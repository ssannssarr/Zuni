# Contributing

Contributions of all sizes are welcome: bug fixes, features, docs and ideas.

## Setup

```bash
git clone https://github.com/ssannssarr/Zuni.git
cd Zuni
uv sync
uv run zuni --help
```

## Preview the docs

```bash
uv run mkdocs serve
```

Open `http://127.0.0.1:8000`.

## Workflow

1. Fork the repository
2. Create a branch

    ```bash
    git checkout -b feature/my-change
    ```

3. Make your changes
4. Test them locally
5. Commit with a clear message
6. Push and open a pull request

## Commit messages

Use short, descriptive messages:

```text
feat: add streaming responses
fix: handle missing config file
docs: expand installation guide
```

| Prefix | Use for |
|--------|---------|
| `feat` | New features |
| `fix` | Bug fixes |
| `docs` | Documentation |
| `refactor` | Code cleanup with no behavior change |

## Code guidelines

- Keep functions small and documented
- Use type hints
- Prefer async code for network calls
- Follow the existing style
- Never commit API keys or config files

## Documentation guidelines

- Update the docs when behavior changes
- Add runnable examples
- Keep pages short and scannable

## Good first contributions

- Better error messages for failed API calls
- Handling a missing config file gracefully
- Tests for `config.py` and `llm.py`
- Improving the docs

## Reporting issues

Open an issue at [github.com/ssannssarr/Zuni/issues](https://github.com/ssannssarr/Zuni/issues) and include:

- The command you ran
- The full output or error
- Your OS and Python version (`python --version`)
- Your Zuni version

!!! warning
    Remove API keys from any logs before posting.

## License

By contributing, you agree your work is released under the [MIT License](https://github.com/ssannssarr/Zuni/blob/main/LICENSE).
