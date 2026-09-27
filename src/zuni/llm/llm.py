"This file is fro actual llm calling"
import json
from typing import Any
import httpx as ht


class LLM:
    """
    This is class for calling llm api from https://openrouter.ai
    """

    def __init__(
        self,
        api_key: str,
        model: str,
    ) -> None:
        """
        Declaring the api_key and model value.
        """
        self.api_key = api_key
        self.model = model
        self.aclient = ht.AsyncClient(
            base_url="https://openrouter.ai/api/v1",
        )

    def headers(
        self
    ) -> dict[str, Any]:
        """
        Constructing the headers.
        """
        key = self.api_key
        if not key:
            raise RuntimeError(
                "No api_key found in self.api_key in class LLM in file llm.py"
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
        payload = {
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
    ) -> None:
        """
        the main process does here.
        """
        headers = self.headers()
        payload = self.payload(
            chat=chat,
            tools=tools
        )

        async with self.aclient.post(
            url="/chat/completions",
            headers=headers,
            json=payload
        ) as res:
            res.raise_for_status()
            return res.json()
