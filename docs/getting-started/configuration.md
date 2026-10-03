# Configuration

Zuni connects to an OpenAI-compatible `/chat/completions` endpoint. The default base URL is OpenRouter when no other base URL is configured.

## Interactive setup

The simplest way to configure Zuni is:

```bash
zuni config
```

You will be asked for three values:

| Prompt | Purpose | Example |
|--------|---------|---------|
| API key | Credential used to access the model API | `sk-or-v1-...` |
| Model ID | Model identifier accepted by the provider | `openrouter/free` |
| Base URL | API root, without `/chat/completions` | `https://openrouter.ai/api/v1` |

The values are saved to:

```text
~/.config/zuni/config.json
```

## Configuration file

A typical configuration looks like this:

```json
{
    "API_KEY": "your-api-key",
    "MODEL": "openrouter/free",
    "BASE_URL": "https://openrouter.ai/api/v1"
}
```

Keep this file private because it can contain your API key.

## Environment variables

| Variable | Purpose |
|----------|---------|
| `ZUNI_API_KEY` | Overrides `API_KEY` from the config file |
| `ZUNI_BASE_URL` | Overrides `BASE_URL` from the config file |

=== "Bash / Zsh"

    ```bash
    export ZUNI_API_KEY="your-api-key"
    export ZUNI_BASE_URL="https://openrouter.ai/api/v1"
    ```

=== "Fish"

    ```fish
    set -Ux ZUNI_API_KEY "your-api-key"
    set -Ux ZUNI_BASE_URL "https://openrouter.ai/api/v1"
    ```

=== "PowerShell"

    ```powershell
    $env:ZUNI_API_KEY = "your-api-key"
    $env:ZUNI_BASE_URL = "https://openrouter.ai/api/v1"
    ```

## Resolution order

### API key

1. `ZUNI_API_KEY`
2. `API_KEY` in `config.json`
3. Error

### Model

1. `MODEL` in `config.json`
2. `openrouter/free`

### Base URL

1. `ZUNI_BASE_URL`
2. `BASE_URL` in `config.json`
3. The default URL in the LLM client

## Provider examples

=== "OpenRouter"

    ```text
    Base URL: https://openrouter.ai/api/v1
    Model ID: openrouter/free
    ```

=== "OpenAI"

    ```text
    Base URL: https://api.openai.com/v1
    Model ID: <your-model>
    ```

=== "Local Ollama"

    ```text
    Base URL: http://localhost:11434/v1
    Model ID: <your-model>
    API key: ollama
    ```

Zuni can work with providers that implement the OpenAI-compatible `POST /chat/completions` interface. Tool calling also requires support for the `tools` request format.

## Security

!!! warning
    Never commit your API key or `config.json` to Git. If an API key is exposed, revoke it through the provider and create a replacement.

On Linux, macOS, and Termux, you can restrict access to the configuration file:

```bash
chmod 600 ~/.config/zuni/config.json
```

## Reset configuration

Remove the configuration file and run setup again:

```bash
rm ~/.config/zuni/config.json
zuni config
```