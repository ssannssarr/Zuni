# Project Structure

```text
Zuni/
├── README.md
├── LICENSE
├── pyproject.toml
├── .python-version
├── mkdocs.yml
├── docs/
│   ├── index.md
│   ├── roadmap.md
│   ├── stylesheets/home.css
│   ├── getting-started/
│   ├── guide/
│   └── development/
└── src/
    └── zuni/
        ├── __init__.py
        ├── cli.py
        ├── llm/
        │   ├── __init__.py
        │   ├── config.py
        │   └── llm.py
        └── prompts/
            ├── prompt.py
            └── system.md
```

## Key files

| File | Purpose |
|------|---------|
| `pyproject.toml` | Metadata, dependencies and the `zuni` script entry |
| `.python-version` | Python version used by uv (`3.14`) |
| `src/zuni/cli.py` | CLI commands |
| `src/zuni/llm/config.py` | Configuration loading and saving |
| `src/zuni/llm/llm.py` | API client |
| `src/zuni/prompts/system.md` | System prompt |
| `mkdocs.yml` | Documentation site settings |
| `docs/stylesheets/home.css` | Home page styling |

## `pyproject.toml` at a glance

```toml
[project]
name = "zuni"
requires-python = ">=3.14"

[project.scripts]
zuni = "zuni.cli:main"

[build-system]
build-backend = "uv_build"
```

The `zuni` command points to the `main` group in `zuni/cli.py`.

## Tooling

| Area | Tool |
|------|------|
| Build backend | `uv_build` |
| Package manager | `uv` |
| Python | 3.14 |
| Docs | MkDocs Material (dev dependency) |
| License | MIT |

## Adding a new command

1. Open `src/zuni/cli.py`
2. Add a function under the `main` group:

    ```python
    @main.command()
    async def hello():
        """Say hello."""
        ac.echo("Hello from Zuni!")
    ```

3. Run `uv run zuni hello`
4. Document it in `docs/guide/commands.md`

## Adding a new prompt

1. Create `src/zuni/prompts/my_prompt.md`
2. Register it in `prompt.py`:

    ```python
    def Prompt() -> dict[str, str]:
        return {
            "system": extract_prompt("system.md"),
            "my_prompt": extract_prompt("my_prompt.md"),
        }
    ```
