"This file is for Configuration purposes"
import os
import json
from pathlib import Path

# Declaring Configuration Dir/Files
HOME = Path.home()
DIR = Path(
    HOME / ".config" / "zuni"
)
FILE = Path(
    DIR / "config.json"
)


def check_dir():
    """
    Checks that Configuration DIR exists or NOT!
    """
    if not DIR.exists():
        raise RuntimeError("Configuration DIR doesn't exists!")


def api_key() -> str:
    """
    This Checks for API_KEY in two steps:

    1. First it checks user's Envioroment for `OPENROUTER_API_KEY` value.
      (if not found)

    2. It checks for if config file exists or not.
        (if config file now it checks if API_KEY value exists or not)

    IF in this two steps API_KEY is not found raise `RuntimeError` with relevant message
    """
    if os.getenv("OPENROUTER_API_KEY"):
        return os.getenv("OPENROUTER_API_KEY")

    if FILE.exists():
        config = json.load(FILE)
        if config.API_KEY:
            return config.API_KEY
        raise RuntimeError(
            "Configuration File does exist but API_KEY is not present their."
        )
    raise RuntimeError("API_KEY is not present in env or config file.")
