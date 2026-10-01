# Installation

Get Zuni running in under a minute.

## Requirements

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.14 or newer | Check with `python --version` |
| uv | latest | Fast Python package and tool manager |
| API key | any | OpenRouter or any OpenAI-compatible provider |
| Internet | required | Zuni calls a hosted model |

## 1. Install uv

=== "Linux / macOS"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows (PowerShell)"

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

=== "pip"

    ```bash
    pip install uv
    ```

Restart your terminal, then confirm:

```bash
uv --version
```

## 2. Install Zuni

```bash
uv tool install git+https://github.com/ssannssarr/Zuni
```

This installs `zuni` in its own isolated environment and puts the command on your `PATH`.

## 3. Verify

```bash
zuni --help
```

You should see the `ask` and `config` commands listed.

## 4. Configure

```bash
zuni config
```

Continue with [Configuration](configuration.md).

## Install from source

Use this if you want to edit the code.

```bash
git clone https://github.com/ssannssarr/Zuni.git
cd Zuni
uv sync
uv run zuni --help
```

!!! tip
    Run `uv tool install --editable .` inside the repo to get a global `zuni` command that reflects your local changes.

## Update

```bash
uv tool upgrade zuni
```

## Uninstall

```bash
uv tool uninstall zuni
rm -rf ~/.config/zuni   # optional: remove saved configuration
```

## If the command is not found

Make sure uv's tool directory is on your `PATH`:

```bash
uv tool update-shell
```

Then restart your terminal. More fixes are in [Troubleshooting](../guide/troubleshooting.md).
