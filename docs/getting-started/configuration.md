# Configuration

Zuni works with any **OpenAI-compatible** API. OpenRouter is the default.

## Interactive setup

```bash
zuni config
```

| Prompt | What to enter | Example |
|--------|---------------|---------|
| API key | Your provider key (hidden while typing) | `sk-or-v1-...` |
| Model ID | The model you want to use | `openrouter/free` |
| Base URL | The API root of your provider | `https://openrouter.ai/api/v1` |

## Config file

Settings are stored here:

| OS | Path |
|----|------|
| Linux / macOS / Termux | `~/.config/zuni/config.json` |
| Windows | `C:\Users\<you>\.config\zuni\config.json` |

```json
{
    "API_KEY": "your-api-key",
    "MODEL": "openrouter/free",
    "BASE_URL": "https://openrouter.ai/api/v1"
}
```

You can edit this file by hand at any time.

## Environment variables

| Variable | Overrides | Required |
|----------|-----------|----------|
| `OPENROUTER_API_KEY` | `API_KEY` in the config file | No |
| `ZUNI_BASE_URL` | `BASE_URL` in the config file | No |

=== "Bash / Zsh"

    ```bash
    export OPENROUTER_API_KEY="your-api-key"
    export ZUNI_BASE_URL="https://openrouter.ai/api/v1"
    ```

=== "Fish"

    ```fish
    set -Ux OPENROUTER_API_KEY "your-api-key"
    set -Ux ZUNI_BASE_URL "https://openrouter.ai/api/v1"
    ```

=== "PowerShell"

    ```powershell
    $env:OPENROUTER_API_KEY = "your-api-key"
    $env:ZUNI_BASE_URL = "https://openrouter.ai/api/v1"
    ```

Add the export line to `~/.bashrc` or `~/.zshrc` to make it permanent.

## How values are resolved

| Value | 1st choice | 2nd choice | Fallback |
|-------|-----------|------------|----------|
| API key | `OPENROUTER_API_KEY` | config file | error |
| Model | config file | none | `openrouter/free` |
| Base URL | `ZUNI_BASE_URL` | config file | none |

!!! note
    The config file should exist even if you use environment variables, because the model is always read from it. Run `zuni config` once to create it.

## Provider examples

=== "OpenRouter"

    ```text
    Base URL: https://openrouter.ai/api/v1
    Model ID: openrouter/free
    ```

=== "OpenAI"

    ```text
    Base URL: https://api.openai.com/v1
    Model ID: gpt-4o-mini
    ```

=== "Local (Ollama)"

    ```text
    Base URL: http://localhost:11434/v1
    Model ID: llama3.2
    API key:  ollama   (any non-empty value)
    ```

Any provider that supports `POST /chat/completions` will work.

## Security

!!! warning
    Never commit your API key or `config.json` to Git. If a key leaks, revoke it from your provider dashboard immediately.

Tighten file permissions on Linux, macOS and Termux:

```bash
chmod 600 ~/.config/zuni/config.json
```

## Reset

```bash
rm ~/.config/zuni/config.json
zuni config
```
