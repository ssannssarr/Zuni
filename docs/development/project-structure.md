# Project Structure

Zuni keeps its main responsibilities separated across the CLI, LLM client, agent, search layer, tools, prompts, and documentation.

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

| Path | Responsibility |
|------|----------------|
| `src/zuni/cli.py` | CLI commands, execution flow, and terminal output |
| `src/zuni/agent.py` | Tool-calling loop |
| `src/zuni/errors.py` | Zuni exception types |
| `src/zuni/llm/config.py` | Configuration loading and saving |
| `src/zuni/llm/llm.py` | OpenAI-compatible API client |
| `src/zuni/prompts/prompt.py` | Prompt loading |
| `src/zuni/prompts/system.md` | Base system prompt |
| `src/zuni/search/search.py` | HTTP requests and DuckDuckGo parsing |
| `src/zuni/tools/schema.py` | Tool definitions sent to the model |
| `src/zuni/tools/toolbox.py` | Tool dispatch and source tracking |
| `src/zuni/tools/web_search.py` | Search and page enrichment |
| `src/zuni/tools/extract_markdown.py` | HTML-to-Markdown extraction |

## Packaging

`pyproject.toml` contains the package metadata, runtime dependencies, Python requirement, and console-script entry point:

```toml
[project.scripts]
zuni = "zuni.cli:main"
```

The repository uses Python 3.14 for development, while the package metadata supports Python 3.11 and newer.

## Changing a command

When adding or changing a command:

1. Update `src/zuni/cli.py`.
2. Test it with `uv run zuni ...`.
3. Update [Commands](../guide/commands.md).
4. Update the architecture page if the execution flow changes.

## Adding a tool

A tool has three main parts:

1. A schema in `src/zuni/tools/schema.py`.
2. Dispatch logic in `src/zuni/tools/toolbox.py`.
3. The implementation in the relevant search or tool module.

The schema name and dispatcher name must remain consistent.

## Documentation

Preview the documentation locally with:

```bash
uv run mkdocs serve
```

When code behavior changes, update the corresponding documentation page in the same change whenever practical.