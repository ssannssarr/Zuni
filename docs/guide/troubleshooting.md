# Troubleshooting

This page covers common installation, configuration, network, and model issues.

## `zuni: command not found`

Refresh uv's shell integration:

```bash
uv tool update-shell
```

Restart your terminal and try again.

## Configuration file errors

If Zuni reports that the configuration file does not exist, run:

```bash
zuni config
```

The default configuration path is:

```text
~/.config/zuni/config.json
```

## API key errors

You can provide the key through the environment:

```bash
export ZUNI_API_KEY="your-api-key"
```

Or run `zuni config`.

The current implementation reads `ZUNI_API_KEY`; it does not use `OPENROUTER_API_KEY` automatically.

## Authentication errors

For HTTP `401` or `403` responses, check:

- the API key
- the provider
- the model ID
- whether the account has access to the selected model

## Model or provider errors

Zuni sends requests to:

```text
{BASE_URL}/chat/completions
```

Check `MODEL` and `BASE_URL` in your configuration and make sure the provider exposes the expected OpenAI-compatible endpoint.

## Rate limits

The LLM client retries temporary failures, including HTTP `429` and common `5xx` responses. If the provider continues returning errors, wait and try again or select another model.

## Connection or timeout errors

Check your:

- internet connection
- base URL
- provider availability
- firewall or network restrictions
- VPN configuration

The LLM client currently uses a 60-second default timeout and retries temporary failures.

## Web search fails

DuckDuckGo can temporarily limit automated requests. If web search fails, Zuni can continue without results or use its search-first fallback when the selected model cannot use tools.

For questions that do not require web research:

```bash
zuni ask --no-search "Explain recursion"
```

## The model does not support tools

Tool calling is not available from every OpenAI-compatible model or provider.

When the first tool-enabled request fails, Zuni falls back to:

```text
web search → collect sources → normal LLM request
```

This fallback is simpler than the normal agent workflow, but it still gives the model the collected source material.

## Answers have no citations

Citations depend on the model using the source numbers provided by Zuni.

If an answer has no citations:

1. Check that web research actually ran.
2. Look at the source list printed below the answer.
3. Check whether the answer contains source references such as `[1]`.

Zuni only displays citation numbers that correspond to collected sources.

## A page cannot be fetched

Zuni rejects obvious local, private, or non-HTTP(S) targets when reading model-selected URLs.

A public page can still fail to load because of:

- anti-bot protection
- authentication requirements
- redirects
- network errors
- unusual or unsupported HTML

## Python version

The package supports Python 3.11+. The repository currently uses Python 3.14 for development.

Check your version with:

```bash
python --version
```

## Debug mode

Set `ZUNI_DEBUG` to allow unexpected exceptions to propagate:

```bash
ZUNI_DEBUG=1 zuni ask "your question"
```

Use this when you need a traceback for debugging.

## Still stuck?

Open an issue with:

- the command you ran
- the complete error output
- your OS and Python version
- your Zuni version or commit
- relevant configuration with secrets removed

Never include an API key or access token.