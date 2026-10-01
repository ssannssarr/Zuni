"This file is for collecting prompts md text and distributing"
from pathlib import Path


PROMPTS_DIR = Path(__file__).parent


def extract_prompt(
        path: str | None,
) -> str:
    """
    This extracts and returns the content.
    """
    PROMPT_FILE = PROMPTS_DIR / path

    return PROMPT_FILE.read_text(
        encoding='utf-8'
    )


def Prompt() -> dict[str, str]:
    return {
        "system": extract_prompt("system.md")
    }
