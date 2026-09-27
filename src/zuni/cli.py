"This is main entry point"
from zuni.llm.config import save_config
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


if __name__ == "__main__":
    main()
