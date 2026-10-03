# Architecture

Zuni is an asynchronous CLI built around four main pieces: an OpenAI-compatible LLM client, a small tool-calling agent, web research tools, and a terminal interface.

## High-level flow

```text
zuni ask
   │
   ▼
 cli.py
   │
   ├── --no-search ──► LLM ──► Markdown
   │
   └── research mode
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

The important idea is simple: the model decides when it needs a tool, Zuni executes that tool, and the result is returned to the model as part of the conversation.

## Main components

### `cli.py`

The CLI defines the commands and coordinates each request. It loads configuration and prompts, creates the LLM client and Toolbox, selects direct or research mode, handles the tool-calling fallback, renders Markdown, and prints sources.

### `agent.py`

`run_agent()` implements the tool-calling loop:

```text
LLM request
    ↓
assistant message
    ↓
tool calls?
  ├─ no → final answer
  └─ yes
       ↓
Toolbox.run(...)
       ↓
tool result added to chat
       ↓
LLM request again
```

The current agent allows up to four tool-call rounds by default. If the limit is reached, Zuni asks the model to answer using the information collected so far.

If the first tool-enabled request is rejected, the CLI treats it as a possible tool-support issue and uses the search-first fallback.

### `llm/llm.py`

The `LLM` class builds OpenAI-compatible chat-completion requests. It can attach tool definitions, sends requests asynchronously with `httpx`, retries temporary failures, maps API errors, and extracts assistant messages.

Requests are sent to:

```text
{BASE_URL}/chat/completions
```

### `llm/config.py`

This module loads and saves Zuni's configuration at:

```text
~/.config/zuni/config.json
```

It resolves the API key, model, and base URL from the configuration file and supported environment variables.

### `tools/schema.py`

This module defines the tool schemas sent to the model.

| Tool | Purpose |
|------|---------|
| `web_search` | Search DuckDuckGo and return source material |
| `extract_markdown` | Fetch a public page and extract readable Markdown |

### `tools/toolbox.py`

`Toolbox` connects model tool calls to their Python implementations. It parses arguments, dispatches tools, tracks sources, assigns source numbers, and turns tool failures into results the model can understand.

### `tools/web_search.py`

The web-search tool searches DuckDuckGo and can fetch selected result pages to enrich the returned source material. Page downloads are performed concurrently.

### `search/search.py`

This module provides lower-level HTTP requests, DuckDuckGo parsing, and URL checks used before page fetching.

### `tools/extract_markdown.py`

This module removes common HTML noise such as scripts, navigation, forms, and iframes, then extracts the most relevant page content and converts it to Markdown.

## Sources and citations

Zuni represents a source as:

```text
Source(index, title, url, content)
```

`Toolbox` owns the source list. A source receives a number when it is first registered. Repeated URLs reuse the existing source number.

The final model response can contain citations such as `[1]` and `[2]`. The CLI reads those references and prints the matching source URLs below the answer.

## Direct mode

Use:

```bash
zuni ask --no-search "Explain recursion"
```

Direct mode skips the agent and web tools:

```text
CLI → system prompt + question → LLM → Markdown
```

## Design goals

- **CLI first:** keep the interface small and terminal-friendly.
- **Async:** use asynchronous APIs for network operations.
- **Provider neutral:** work with the common OpenAI-compatible chat-completions format.
- **Tool based:** keep web capabilities behind explicit model-callable tools.
- **Grounded:** retain source information so answers can reference retrieved material.
- **Small core:** keep the agent and tool layer understandable.