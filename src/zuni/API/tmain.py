"""Import Required Dependencies"""
import os
import asyncio
from rich.console import Console
from api import (
    APIConfig,
    OpenAI
)

console = Console()

temp = APIConfig(
    API_KEY=os.getenv("OPENROUTER_API_KEY"),
    BASE_URL="https://openrouter.ai/api",
    MODEL="openrouter/free"
)


chat = []


def add(
    role: str | None,
    content: str | None,
) -> None:
    chat.append({
        "role": role,
        "content": content
    })


ai = OpenAI(config=temp)


async def main():
    add(
        role="user",
        content="hiii"
    )
    try:
        res, success = await ai.ask(
            chat=chat,
        )
        console.print_json(data=res)
    finally:
        await ai.aclose()

if __name__ == "__main__":
    asyncio.run(main())
