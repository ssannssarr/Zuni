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


def save_config(
        api_key: str,
        model: str,
        base_url: str,
) -> None:
    """
    This method save's Configuration values.
    """
    CONFIG_DIR.mkdir(
        parents=True,
        exist_ok=True
    )
    data = {
        "API_KEY": api_key,
        "MODEL": model,
        "BASE_URL": base_url
    }

    CONFIG_FILE.write_text(
        data=json.dumps(
            data,
            indent=4
        ),
        encoding='utf-8',

    )


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


def baseUrl() -> str:
    """
    loads base_url from env or config file.
    """
    url = os.getenv("ZUNI_BASE_URL")
    if url:
        return url

    config = load_config()

    url = config.get("BASE_URL")
    if url:
        return url


def Config() -> dict[str, Any]:
    """
    This method loads both model and api_key value and returns in json format.
    """
    apikey = api_key()
    modelid = model()
    base_url = baseUrl()
    return {
        "API_KEY": apikey,
        "MODEL": modelid,
        "BASE_URL": base_url
    }
