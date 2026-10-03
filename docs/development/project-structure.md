# Project Structure

The repository separates the CLI, LLM client, agent, search layer, tools, prompts, and documentation.

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
│   ├── stylesheets/
│   │   └── home.css
│   ├── getting-started/
│   │   ├── installation.md
│   │   └── configuration.md
│   ├── guide/
│   │   ├── commands.md
│   │   ├── architecture.md
│   │   └── troubleshooting.md
│   └── development/
│       ├── project-structure.md
│       └── contributing.md
└── src/
    └── zuni/
        ├── __init__.py
        ├── cli.py
        ├── agent.py
        ├── errors.py
        ├── llm/
        │   ├── __init__.py
        │   ├── config.py
        │   └── llm.py
        ├── prompts/
        │   ├── prompt.py
        │   └── system.md
        ├── search/
        │   └── search.py
        └── tools/
            ├── schema.py
            ├── toolbox.py
            ├── web_search.py
            └── extract_markdown.py
```

## Core modules

| Path | Purpose |
|------|---------|
| `src/zuni/cli.py` | CLI commands, execution flow, and output rendering |
| `src/zuni/agent.py` | Tool-calling loop |
| `src/zuni/errors.py` | Zuni exception types |
| `src/zuni/llm/config.py` | Configuration loading and saving |
| `src/zuni/llm/llm.py` | OpenAI-compatible API client |
| `src/zuni/prompts/prompt.py` | Prompt loading |
| `src/zuni/prompts/system.md` | Base system prompt |
| `src/zuni/search/search.py` | HTTP requests and DuckDuckGo parsing |
| `src/zuni/tools/schema.py` | Tool definitions sent to the model |
| `src/zuni/tools/toolbox.py` | Tool dispatch and source tracking |
| `src/zuni/tools/web_search.py` | Search plus page enrichment |
| `src/zuni/tools/extract_markdown.py` | HTML-to-Markdown extraction |

## Packaging

`pyproject.toml` contains package metadata, runtime dependencies, the Python requirement, and the `zuni` console-script entry point:

```toml
[project.scripts]
zuni = "zuni.cli:main"
```

The repository's `.python-version` currently uses Python 3.14 for development, while package metadata supports Python 3.11+.

## Adding or changing a command

1. Update the command in `src/zuni/cli.py`.
2. Test it with `uv run zuni ...`.
3. Update [Commands](../guide/commands.md).
4. Update architecture documentation if the execution flow changed.

## Adding a tool

A tool has three important pieces:

1. Schema in `src/zuni/tools/schema.py`.
2. Execution in `src/zuni/tools/toolbox.py`.
3. Implementation in the relevant search/tool module.

The schema name and dispatcher name must match.

## Documentation

Run the local documentation server with:

```bash
uv run mkdocs serve
```

When code behavior changes, update the corresponding documentation page in the same change whenever possible.