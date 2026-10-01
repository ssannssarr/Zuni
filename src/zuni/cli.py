"This is main entry point"
from zuni.llm.config import (
    save_config,
    Config
)
from zuni.llm.llm import LLM
from zuni.prompts.prompt import Prompt
from rich.console import Console
from rich.markdown import Markdown as md
import asyncclick as ac

console = Console()


@ac.group()
async def main():
    """
    This creats a cli group.
    So, all the commands stays at one place.
    """
    pass


@main.command()
async def config():
    """
    This method is for setting config values.
    """
    api_key = await ac.prompt(
        "Enter your API key",
        hide_input=True
    )
    model = await ac.prompt(
        "Enter model ID"
    )
    base_url = await ac.prompt(
        "Enter Base Url"
    )

    save_config(
        api_key=api_key,
        model=model,
        base_url=base_url
    )

    ac.echo("Configuration saved.")


@main.command()
@ac.argument(
    "prompt",
    required=True
)
async def ask(
    prompt: str | None = None
):
    """
    This method is for asking an question directly from terminal.
    """
    cnfg = Config()
    llm = LLM(
        api_key=cnfg["API_KEY"],
        model=cnfg["MODEL"],
        base_url=cnfg["BASE_URL"]
    )

    async def msg():
        prmpt = Prompt()
        chat = [
            {
                "role": "system",
                "content": prmpt["system"]
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        res = await llm.ask(chat=chat)
        msg = res["choices"][0]["message"]["content"]
        return msg
    msg = await msg()
    console.print(md(msg))

if __name__ == "__main__":
    main()
