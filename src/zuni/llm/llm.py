"This file is for actual llm calling"
from __future__ import annotations

import asyncio
from typing import Any

import httpx as ht

from zuni.errors import (
    APIError,
    AuthError,
    ConfigError,
    NetworkError,
    RateLimitError,
    ZuniError,
)

DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"

# Statuses that are usually temporary, so retrying makes sense.
RETRY_STATUSES = {429, 500, 502, 503, 504}


class LLM:
    """
    This is class for calling llm api from OpenAI compatible API.

    Temporary failures (timeouts, connection errors, 429, 5xx) are retried
    with exponential backoff. Everything else is turned into a ZuniError
    with a message that is safe to show to the user.
    """

    def __init__(
        self,
        api_key: str,
        model: str,
        base_url: str | None = DEFAULT_BASE_URL,
        timeout: float = 60.0,
        retries: int = 2,
    ) -> None:
        """
        Declaring the api_key, model, base_url and retry settings.

        base_url falls back to OpenRouter when it is empty or None.
        """
        self.api_key = api_key
        self.model = model
        self.base_url = (base_url or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.retries = retries

    def headers(
        self
    ) -> dict[str, Any]:
        """
        Constructing the headers.

        Raises ConfigError if there is no api key.
        """
        key = self.api_key
        if not key:
            raise ConfigError(
                "No API key found. Run `zuni config` "
                "or set OPENROUTER_API_KEY."
            )

        return {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }

    def payload(
        self,
        chat: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        This method builds and returns the payload.
        """
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": chat,
        }

        if tools:
            payload["tools"] = tools

        return payload

    async def ask(
        self,
        chat: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        the main process does here.

        Sends the chat and returns the decoded JSON response.

        Raises:
            NetworkError: could not reach the API.
            AuthError: the key was rejected (401/403).
            RateLimitError: still rate limited after all retries.
            APIError: any other error response, or a malformed one.
        """
        headers = self.headers()
        payload = self.payload(
            chat=chat,
            tools=tools
        )
        url = f"{self.base_url}/chat/completions"
        last_error: ZuniError | None = None

        async with ht.AsyncClient(timeout=self.timeout) as client:
            for attempt in range(self.retries + 1):
                delay = float(2 ** attempt)  # 1s, 2s, 4s...
                try:
                    res = await client.post(
                        url,
                        headers=headers,
                        json=payload
                    )
                except ht.TimeoutException:
                    last_error = NetworkError(
                        f"The request timed out after {self.timeout:.0f}s."
                    )
                except ht.ConnectError:
                    last_error = NetworkError(
                        f"Could not connect to {self.base_url}. "
                        "Check your internet connection and base URL."
                    )
                except ht.HTTPError as exc:
                    last_error = NetworkError(f"Network error: {exc}")
                else:
                    if res.status_code not in RETRY_STATUSES:
                        return self._parse(res)
                    last_error = self._error_for(res)
                    delay = self._retry_after(res, delay)

                if attempt < self.retries:
                    await asyncio.sleep(delay)

        if last_error is None:  # pragma: no cover - cannot happen
            last_error = APIError("The request failed for an unknown reason.")
        raise last_error

    @staticmethod
    def message(
        res: dict[str, Any]
    ) -> dict[str, Any]:
        """
        Returns the assistant message from a response.

        Raises APIError if the response has an unexpected shape.
        """
        try:
            msg = res["choices"][0]["message"]
        except (KeyError, IndexError, TypeError):
            raise APIError(
                "The API response had an unexpected format."
            ) from None
        if not isinstance(msg, dict):
            raise APIError("The API response had an unexpected format.")
        return msg

    @staticmethod
    def text(
        res: dict[str, Any]
    ) -> str:
        """
        Returns only the reply text from a response.

        Raises APIError if the reply is empty.
        """
        content = LLM.message(res).get("content")
        if not content or not str(content).strip():
            raise APIError("The model returned an empty reply. Try again.")
        return str(content)

    # ----- internals ------------------------------------------------------

    def _parse(
        self,
        res: ht.Response
    ) -> dict[str, Any]:
        """
        Turns a final (non-retryable) response into JSON or raises.
        """
        if res.status_code >= 400:
            raise self._error_for(res)
        try:
            data = res.json()
        except ValueError:
            raise APIError("The API returned invalid JSON.") from None
        # Some providers send HTTP 200 with an error body.
        if (
            isinstance(data, dict)
            and "error" in data
            and "choices" not in data
        ):
            raise APIError(f"API error: {self._extract_message(data)}")
        return data

    def _error_for(
        self,
        res: ht.Response
    ) -> ZuniError:
        """
        Maps an HTTP error response to the right exception.
        """
        status = res.status_code
        message = self._message(res)
        if status in (401, 403):
            return AuthError(
                f"The API rejected your key ({status}): {message}"
            )
        if status == 429:
            return RateLimitError(f"Rate limited by the API: {message}")
        return APIError(f"API error {status}: {message}")

    def _message(
        self,
        res: ht.Response
    ) -> str:
        """
        Best-effort human readable message from an error response.
        """
        try:
            return self._extract_message(res.json())
        except ValueError:
            return res.text[:200].strip() or "no details provided"

    @staticmethod
    def _extract_message(
        data: object
    ) -> str:
        """
        Pulls error.message (or error) out of a JSON body.
        """
        if isinstance(data, dict):
            error = data.get("error", data)
            if isinstance(error, dict):
                return str(error.get("message") or error)
            return str(error)
        return str(data)

    @staticmethod
    def _retry_after(
        res: ht.Response,
        default: float
    ) -> float:
        """
        Respects a numeric Retry-After header, capped at 10 seconds.
        """
        value = res.headers.get("retry-after", "")
        try:
            return min(float(value), 10.0)
        except ValueError:
            return default
