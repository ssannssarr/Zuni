# Troubleshooting

## `zuni: command not found`

uv's tool directory is not on your `PATH`.

```bash
uv tool update-shell
```

Restart the terminal and try again.

## `RuntimeError: Configuration File doesn't exists!`

Zuni could not find `~/.config/zuni/config.json`.

```bash
zuni config
```

If `zuni config` itself fails with this error, create the file manually:

```bash
mkdir -p ~/.config/zuni
cat > ~/.config/zuni/config.json <<'JSON'
{
    "API_KEY": "your-api-key",
    "MODEL": "openrouter/free",
    "BASE_URL": "https://openrouter.ai/api/v1"
}
JSON
```

## `RuntimeError: API_KEY is not present in env or config file.`

No key was found. Set one:

```bash
export OPENROUTER_API_KEY="your-api-key"
```

or run `zuni config`.

## `KeyError: 'choices'`

The API returned an error instead of an answer. Common causes:

| Cause | Fix |
|-------|-----|
| Invalid or expired API key | Create a new key and run `zuni config` |
| Wrong model ID | Check the exact ID on your provider's model list |
| Rate limit or no credits | Wait, or switch to a free model |
| Wrong base URL | It must end at the API root, such as `/v1` |

## Connection or timeout errors

- Check your internet connection
- Confirm the base URL has no typos
- Try again later if the provider is down

## Python version error

Zuni needs Python 3.14 or newer.

```bash
python --version
uv python install 3.14
```

## The answer looks plain or unformatted

Formatting only appears when printing to a terminal. Redirecting output to a file (`> file.txt`) removes it.

## Docs page looks outdated

Hard refresh the browser, or clear the site cache, so the latest CSS loads.

## Still stuck?

Open an issue with your command, full error and Python version: [github.com/ssannssarr/Zuni/issues](https://github.com/ssannssarr/Zuni/issues).
