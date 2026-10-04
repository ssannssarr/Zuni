# Installation

Get Zuni installed and ready to use from your terminal.

## Requirements

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.11+ | Minimum version supported by the package |
| uv | Latest | Recommended for installation and project management |
| API key | Provider-dependent | Required when using a hosted model API |
| Internet access | Required for web research | Not required for a local model used without web tools |

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

Verify the installation:

```bash
uv --version
```

## Install Zuni

Zuni is published on PyPI. Install the latest release with:

```bash
uv tool install ssannssarr.zuni
```

Then verify the command:

```bash
zuni --help
```

You should see the `ask` and `config` commands.

!!! tip
    If you want to install a specific release, append the version, for example `uv tool install ssannssarr.zuni==0.1.0`.

## Configure Zuni

Run:

```bash
zuni config
```

Zuni will ask for your API key, model ID, and base URL. See [Configuration](configuration.md) for details.

## Install from source

For development or local changes:

```bash
git clone https://github.com/ssannssarr/Zuni.git
cd Zuni
uv sync
uv run zuni --help
```

!!! tip
    Use `uv tool install --editable .` from the repository if you want a global `zuni` command that follows your local source changes.

## Update

For a PyPI installation:

```bash
uv tool upgrade zuni
```

For a source checkout:

```bash
git pull
uv sync
```

## Uninstall

Remove the tool installation with:

```bash
uv tool uninstall zuni
```

If you also want to remove the local configuration:

```bash
rm -rf ~/.config/zuni
```

## If the command is not found

Refresh uv's shell integration:

```bash
uv tool update-shell
```

Restart your terminal and try again. If the problem continues, see [Troubleshooting](../guide/troubleshooting.md).
