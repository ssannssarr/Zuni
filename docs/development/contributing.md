# Contributing

Contributions are welcome in code, documentation, bug fixes, testing, and project ideas.

## Development setup

Clone the repository and install its development dependencies:

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

Start the local MkDocs server:

```bash
uv run mkdocs serve
```

Open the local address shown by MkDocs and check both the homepage and regular documentation pages.

## Workflow

A typical contribution looks like this:

1. Fork the repository.
2. Create a focused branch.
3. Make the change.
4. Run the relevant commands locally.
5. Update documentation when behavior changes.
6. Commit the change with a clear message.
7. Push the branch and open a pull request.

For example:

```bash
git checkout -b feature/my-change
```

## Commit messages

Keep commit messages short and descriptive:

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
| `docs` | Documentation changes |
| `refactor` | Internal restructuring |

## Code guidelines

- Keep functions focused and easy to follow.
- Use type hints where practical.
- Prefer asynchronous APIs for network operations.
- Keep user-facing errors clear and actionable.
- Never commit API keys or local configuration files.
- Treat model-controlled network access as untrusted input.

## Tool and web-search changes

When modifying a tool:

- keep its schema and implementation in sync
- validate required arguments
- preserve useful error messages
- avoid exposing secrets in tool output
- consider URL and redirect safety
- update the architecture documentation when behavior changes

## Documentation guidelines

Documentation should describe the current implementation.

- Keep examples runnable.
- Prefer short sections and clear headings.
- Explain behavior before implementation details.
- Update links when pages move.
- Keep architecture documentation synchronized with the code.
- Avoid presenting planned features as if they already exist.

## Areas for contribution

Some useful areas include:

- agent and tool tests
- configuration handling
- URL safety
- error handling
- documentation
- CI
- packaging

## Reporting a bug

When opening an issue, include:

- the command you ran
- the complete error output
- your OS and Python version
- your Zuni version or commit
- relevant configuration with secrets removed

!!! warning
    Never include API keys, access tokens, or private configuration values in an issue.

## License

By contributing, you agree that your contribution is released under the project's [MIT License](https://github.com/ssannssarr/Zuni/blob/main/LICENSE).