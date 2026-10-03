# Architecture

Zuni is an asynchronous CLI built around an OpenAI-compatible LLM client, a small tool-calling agent, and web research tools.

## High-level flow

```text
zuni ask
   │
   ▼
 cli.py
   │
   ├── --no-search ──► LLM ──► Markdown
   │
   └── search mode
          │
          ▼
       Agent loop
          │
      ┌───┴───────────┐
      ▼               ▼
 web_search     extract_markdown
      │               │
      └───────┬───────┘
              ▼
          tool results
              │
              ▼
             LLM
              │
              ▼
       Markdown + sources
```

## Main components

### `cli.py`

The CLI defines commands, loads configuration and prompts, creates the LLM client and Toolbox, selects direct or research mode, handles the no-tool-calling fallback, renders Markdown, and prints sources.

### `agent.py`

`run_agent()` implements the tool-calling loop:

```text
LLM request
    ↓
assistant message
    ↓
tool_calls?
  ├─ no → final answer
  └─ yes
       ↓
Toolbox.run(...)
       ↓
tool result appended to chat
       ↓
LLM request again
```

The current agent has a default maximum of four tool-call rounds. When that budget is exhausted, Zuni asks the model to answer using the information gathered so far.

If the first tool-enabled request fails, the CLI treats that as possible lack of tool support and uses the search-first fallback.

### `llm/llm.py`

The `LLM` class builds OpenAI-compatible chat-completion requests, optionally attaches tool definitions, sends them asynchronously with `httpx`, retries temporary failures, maps API errors, and extracts assistant messages.

Requests are sent to:

```text
{BASE_URL}/chat/completions
```

### `llm/config.py`

Configuration lives at `~/.config/zuni/config.json`. The module resolves the API key, model, and base URL from the config file and supported environment variables.

### `tools/schema.py`

This module defines the tool schemas sent to the model.

| Tool | Purpose |
|------|---------|
| `web_search` | Search DuckDuckGo and return numbered sources |
| `extract_markdown` | Download a specific public page and extract readable Markdown |

### `tools/toolbox.py`

`Toolbox` is the execution layer between model tool calls and Python functions. It parses arguments, dispatches tool names, tracks sources, assigns source numbers, and returns tool failures as text.

### `tools/web_search.py`

The web-search tool combines DuckDuckGo results with best-effort fetching of the top pages and converts fetched HTML into compact Markdown. Up to three page downloads run concurrently.

### `search/search.py`

This module handles lower-level HTTP requests, DuckDuckGo HTML parsing, and public URL checks before page fetching.

### `tools/extract_markdown.py`

HTML is cleaned by removing common noise such as scripts, navigation, forms, and iframes. Zuni prefers `article`, `main`, or `body` content and converts it to compact Markdown.

## Sources and citations

Sources are represented as:

```text
Source(index, title, url, content)
```

`Toolbox` owns the source list. A source receives a number when first registered. Repeated URLs reuse the existing source number.

The final model response can cite sources as `[1]`, `[2]`, and so on. The CLI extracts those references and prints the corresponding URLs below the answer.

## Direct mode

```bash
zuni ask --no-search "Explain recursion"
```

Direct mode skips the agent and tools:

```text
CLI → system prompt + question → LLM → Markdown
```

## Design goals

- **CLI first:** keep the interface small and terminal-friendly.
- **Async:** network operations use asynchronous APIs.
- **Provider neutral:** use the common OpenAI-compatible chat-completions format.
- **Tool based:** keep web capabilities behind explicit model-callable tools.
- **Grounded:** preserve source information so answers can cite retrieved material.
- **Small core:** keep the agent and tool layer understandable.