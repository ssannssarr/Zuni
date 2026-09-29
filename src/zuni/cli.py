"This is main entry point"
from zuni.llm.config import (
    save_config,
    Config
)
from zuni.llm.llm import LLM
import asyncclick as ac


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


if __name__ == "__main__":
    main()
