# Configuration

Zuni uses an OpenAI-compatible `/chat/completions` API. OpenRouter is the default base URL when no base URL is supplied.

## Interactive setup

```bash
zuni config
```

Zuni asks for three values:

| Prompt | Description | Example |
|--------|-------------|---------|
| API key | Credential used for the model API | `sk-or-v1-...` |
| Model ID | Model identifier accepted by your provider | `openrouter/free` |
| Base URL | API root, without `/chat/completions` | `https://openrouter.ai/api/v1` |

The values are saved to:

```text
~/.config/zuni/config.json
```

## Config file

```json
{
    "API_KEY": "your-api-key",
    "MODEL": "openrouter/free",
    "BASE_URL": "https://openrouter.ai/api/v1"
}
```

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
3. OpenRouter's default URL in the LLM client

!!! note
    Running `zuni config` once is the simplest setup because Zuni reads the model and base URL from the configuration module.

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

Any provider that accepts the OpenAI-compatible `POST /chat/completions` format can be used. Tool calling additionally depends on model/provider support.

## Security

!!! warning
    Never commit your API key or `config.json` to Git. If a key leaks, revoke it from your provider immediately.

On Linux, macOS, and Termux:

```bash
chmod 600 ~/.config/zuni/config.json
```

## Reset configuration

```bash
rm ~/.config/zuni/config.json
zuni config
```