"""Import Required dependenies"""
from typing import Any
from dataclasses import dataclass
import httpx


@dataclass(frozen=True)
class APIConfig:
    API_KEY: str | None
    BASE_URL: str | None
    MODEL: str | None
    TIMEOUT: int | None = 60


class OpenAI:

    def __init__(self, config: APIConfig):
        self.api_key = config.API_KEY
        self.base_url = config.BASE_URL
        self.model = config.MODEL
        self.timeout = config.TIMEOUT
        self.aclient = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout
        )

    def headers(self) -> dict[str, Any]:
        if not self.api_key:
            raise RuntimeError("API Key not found in config")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        return headers

    def payload(
        self,
        chat: list[dict[str, Any]] | None,
        tools: list[dict[str, Any]] | None = None,
    ) -> list[dict[str, Any]]:
        payload = {
            "model": self.model,
            "messages": chat
        }
        if tools is not None:
            payload["tools"] = tools

        return payload

    async def ask(
        self,
        chat: list[dict[str, Any]] | None,
        tools: list[dict[str, Any]] | None = None,
    ) -> list[dict[str, Any]]:

        response = await self.aclient.post(
            "/v1/chat/completions",
            headers=self.headers(),
            json=self.payload(
                chat=chat,
                tools=tools
            )
        )

        if response.status_code == 200:
            return response.json(), True
        return response.json(), False

    async def aclose(self):
        await self.aclient.aclose()
