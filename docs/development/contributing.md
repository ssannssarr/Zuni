# Contributing

Contributions are welcome across code, documentation, bug fixes, and ideas.

## Development setup

```bash
git clone https://github.com/ssannssarr/Zuni.git
cd Zuni
uv sync
uv run zuni --help
```

For a global editable installation:

```bash
uv tool install --editable .
```

## Preview the documentation

```bash
uv run mkdocs serve
```

## Workflow

1. Fork the repository.
2. Create a focused branch.
3. Make the change.
4. Run relevant commands locally.
5. Update documentation when behavior changes.
6. Commit with a clear message.
7. Push and open a pull request.

Example branch:

```bash
git checkout -b feature/my-change
```

## Commit messages

```text
feat: add streaming responses
fix: handle missing config file
docs: expand installation guide
refactor: simplify tool dispatch
```

| Prefix | Use for |
|--------|---------|
| `feat` | New features |
| `fix` | Bug fixes |
| `docs` | Documentation |
| `refactor` | Internal restructuring |

## Code guidelines

- Keep functions focused.
- Use type hints.
- Prefer async APIs for network operations.
- Keep user-facing errors understandable.
- Do not commit API keys or local configuration files.
- Be careful when changing model-controlled network access.

## Tool and web-search changes

When modifying a tool:

- keep its schema and implementation consistent
- validate required arguments
- preserve useful error messages
- avoid exposing secrets in tool output
- consider URL and redirect safety
- update the architecture documentation

## Documentation guidelines

- Document current behavior, not planned behavior.
- Keep examples runnable.
- Keep pages short and scannable.
- Update links when pages move.
- Keep architecture documentation synchronized with the code.

## Useful contribution areas

Current areas that can use work include stronger agent tests, configuration handling, URL safety, error handling, documentation, CI, and packaging.

## Reporting a bug

Open an issue and include:

- command you ran
- full error output
- OS and Python version
- Zuni version or commit
- relevant configuration with secrets removed

!!! warning
    Never include API keys, access tokens, or private configuration values in an issue.

## License

By contributing, you agree that your contribution is released under the project's [MIT License](https://github.com/ssannssarr/Zuni/blob/main/LICENSE).