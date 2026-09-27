"This is main entry point"
from zuni.llm.config import save_config
import asyncclick as click


@click.group
def main():
    """
    This creats a cli group.
    So, all the commands stays at one place.
    """
    pass


@main.command()
async def config():
    api_key = await click.prompt(
        "Enter your API key",
        hide_input=True
    )
    model = await click.prompt(
        "Enter model ID"
    )
    base_url = await click.prompt(
        "Enter Base Url"
    )

    save_config(
        api_key=api_key,
        model=model,
        base_url=base_url
    )

    click.echo("Configuration saved.")


if __name__ == "__main__":
    main()
