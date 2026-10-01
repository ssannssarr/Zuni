# Architecture

Zuni is a small async CLI. It sends one question to an OpenAI-compatible API and renders the reply.

## Request flow

```text
zuni ask "question"
      │
      ▼
   cli.py ──────────► prompts/  (load system prompt)
      │
      ▼
   llm/config.py     (API key, model, base URL)
      │
      ▼
   llm/llm.py ──────► POST /chat/completions
      │
      ▼
   rich renders the Markdown answer
```

## Modules

### `cli.py`

Entry point registered as `zuni` in `pyproject.toml`.

- Defines the `main` command group
- `config` command: prompts for settings and saves them
- `ask` command: builds the chat and prints the reply

### `llm/config.py`

Handles configuration.

| Function | Purpose |
|----------|---------|
| `api_key()` | Reads the key from `OPENROUTER_API_KEY`, then the config file |
| `model()` | Reads the model from the config file, defaults to `openrouter/free` |
| `baseUrl()` | Reads `ZUNI_BASE_URL`, then the config file |
| `load_config()` | Loads `~/.config/zuni/config.json` |
| `save_config()` | Writes the config file |
| `Config()` | Returns all three values as a dictionary |

### `llm/llm.py`

The `LLM` class wraps the API call.

| Method | Purpose |
|--------|---------|
| `headers()` | Builds the `Authorization` and `Content-Type` headers |
| `payload()` | Builds the request body (model, messages, optional tools) |
| `ask()` | Sends the request with `httpx.AsyncClient` and returns the JSON |

### `prompts/`

| File | Purpose |
|------|---------|
| `prompt.py` | Reads prompt files and exposes them through `Prompt()` |
| `system.md` | System prompt that defines Zuni's behavior |

## Request payload

```json
{
    "model": "openrouter/free",
    "messages": [
        { "role": "system", "content": "You are Zuni..." },
        { "role": "user", "content": "Explain how DNS works" }
    ]
}
```

## Response handling

The reply is read from:

```text
response["choices"][0]["message"]["content"]
```

and rendered with `rich.markdown.Markdown`.

## Dependencies

| Package | Used for |
|---------|----------|
| `asyncclick` | Async command-line interface |
| `httpx` | Async HTTP client |
| `rich` | Markdown rendering in the terminal |

## System prompt rules

`system.md` sets these behaviors:

- Be accurate, concise and useful
- Never fabricate information and state uncertainty
- Cite only sources that were provided
- Break complex problems into steps
- Avoid greetings and filler, optimize for the terminal
- Decline harmful requests and offer a safe alternative

## Design choices

- **Async first:** built on `asyncclick` and `httpx` so features like streaming and parallel tool calls fit naturally
- **Provider neutral:** only the standard chat completions format is used
- **Small surface:** two commands, four modules
