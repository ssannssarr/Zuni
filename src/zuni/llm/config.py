"This file is for Configuration purposes"
import os
import json
from pathlib import Path
from typing import Any

# Declaring Configuration Dir/Files
HOME = Path.home()
DIR = HOME / ".config" / "zuni"
FILE = DIR / "config.json"


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

    # This is for checking value in user's local Environment
    key = os.getenv("OPENROUTER_API_KEY")
    if key:
        return key

    # This is for checking value in config file.
    config = load_config()
    key = config.get("API_KEY")
    if key:
        return key

    # This raise's error if API_KEY is not found in both places
    raise RuntimeError("API_KEY is not present in env or config file.")


def load_config() -> dict[str, Any]:
    """
    This Method loads the Configuration values from the config file
    """
    if FILE.exists():
        with open(FILE) as config:
            data = json.load(config)
            return data
    raise RuntimeError("Configuration File doesn't exists!")


print(api_key())
