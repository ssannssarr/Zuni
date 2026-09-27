"This file is for Configuration purposes"
import json
import os
from pathlib import Path
from typing import Any

# Declaring Configuration Dir/Files
HOME = Path.home()
CONFIG_DIR = HOME / ".config" / "zuni"
CONFIG_FILE = CONFIG_DIR / "config.json"


def api_key() -> str:
    """
    This Checks for API_KEY in two steps:

    1. First it checks user's Envioroment for `OPENROUTER_API_KEY` value.
      (if not found)

    2. It checks for if config file exists or not.
        (if config file now it checks if API_KEY value exists or not)

    IF in this two steps API_KEY is not found
    IT raise `RuntimeError` with relevant message
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
    # Checks Config File Exixst's or Not
    if not CONFIG_FILE.exists():
        raise RuntimeError(
            "Configuration File doesn't exists!"
        )

    # Checks config file and return json values
    with CONFIG_FILE.open(
        "r",
        encoding="utf-8"
    ) as config:
        return json.load(config)


def model() -> str:
    """
    This method loads model id saved in config file.
    If there is no model value in the config file
    Then it returns default model value
    """
    config = load_config()
    model = config.get("MODEL")

    if model:
        return model

    return "openrouter/free"


def Config() -> dict[str, Any]:
    """
    This method loads both model and api_key value and returns in json format.
    """
    apikey = api_key()
    modelid = model()
    return {
        "API_KEY": apikey,
        "MODEL": modelid,
    }
