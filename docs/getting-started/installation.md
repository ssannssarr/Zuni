# Installation

Get Zuni running in a few steps.

## Requirements

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.11+ | Declared package requirement |
| uv | latest | Recommended package and tool manager |
| API key | provider-dependent | Required for hosted model APIs |
| Internet | required for web research | Direct local-model mode can avoid web access |

The repository currently uses Python 3.14 for development through `.python-version`.

## Install uv

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

Verify:

```bash
uv --version
```

## Install Zuni

```bash
uv tool install git+https://github.com/ssannssarr/Zuni
```

Then:

```bash
zuni --help
```

You should see the `ask` and `config` commands.

## Configure

```bash
zuni config
```

Zuni asks for an API key, model ID, and base URL. Continue with [Configuration](configuration.md).

## Install from source

```bash
git clone https://github.com/ssannssarr/Zuni.git
cd Zuni
uv sync
uv run zuni --help
```

!!! tip
    Run `uv tool install --editable .` inside the repository if you want a global `zuni` command that follows local source changes.

## Update

Tool installation:

```bash
uv tool upgrade zuni
```

Source checkout:

```bash
git pull
uv sync
```

## Uninstall

```bash
uv tool uninstall zuni
```

Optionally remove local configuration:

```bash
rm -rf ~/.config/zuni
```

## If the command is not found

```bash
uv tool update-shell
```

Restart your terminal. More fixes are in [Troubleshooting](../guide/troubleshooting.md).