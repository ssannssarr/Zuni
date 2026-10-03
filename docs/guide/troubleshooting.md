# Troubleshooting

## `zuni: command not found`

Update uv's shell integration:

```bash
uv tool update-shell
```

Restart the terminal and try again.

## Configuration file error

If you see `Configuration File doesn't exists!`, run:

```bash
zuni config
```

Zuni stores configuration at `~/.config/zuni/config.json`.

## API key error

Set the current environment variable:

```bash
export ZUNI_API_KEY="your-api-key"
```

or run `zuni config`. The current implementation checks `ZUNI_API_KEY`, not `OPENROUTER_API_KEY`.

## Authentication errors

For HTTP 401 or 403 responses, verify the API key, provider, and model access.

## Model or provider errors

Zuni sends requests to `{BASE_URL}/chat/completions`. Check `MODEL` and `BASE_URL` in your configuration.

## Rate limits

The LLM client retries temporary failures including HTTP 429 and common 5xx responses. If the provider continues returning errors, wait or change models.

## Connection or timeout errors

Check your internet connection, base URL, provider availability, firewall, and VPN. The LLM client uses a 60-second default timeout and retries temporary failures.

## Web search fails

DuckDuckGo may rate-limit automated requests. If search is unavailable, Zuni can return the tool error to the model or use its search-first fallback when tool calling is unavailable.

For questions that do not need research:

```bash
zuni ask --no-search "Explain recursion"
```

## The model does not support tools

Not every OpenAI-compatible model supports tool calling. When the first tool-enabled request fails, Zuni falls back to:

```text
web search → collect sources → normal LLM request
```

## Answers have no citations

Citations depend on the model using the source numbers supplied by Zuni. Check that web research ran and inspect the source list printed below the answer.

Zuni only accepts citation numbers that correspond to collected sources.

## A page cannot be fetched

Zuni rejects obvious local/private/non-HTTP(S) targets when reading model-selected URLs. Public pages can still fail because of anti-bot protection, authentication, redirects, network errors, or unusual HTML.

## Python version

Package metadata supports Python 3.11+. The repository currently uses Python 3.14 for development.

```bash
python --version
```

## Debug mode

Set `ZUNI_DEBUG` to let unexpected exceptions propagate:

```bash
ZUNI_DEBUG=1 zuni ask "your question"
```

## Still stuck?

Open an issue and include the command, full error, OS, Python version, and relevant configuration with secrets removed. Never post your API key.