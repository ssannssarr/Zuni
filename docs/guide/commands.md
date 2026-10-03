# Commands

Zuni currently exposes two commands:

```bash
zuni [COMMAND] [ARGUMENTS]
```

| Command | Purpose |
|---------|---------|
| `zuni ask` | Ask a question and optionally research the web |
| `zuni config` | Save API key, model, and base URL |
| `zuni --help` | Show command help |

---

## `zuni ask`

Ask a question from the terminal.

```bash
zuni ask "Explain how DNS works"
```

Web research is enabled by default. The agent can decide to use the available tools, then return an answer with cited sources.

### Syntax

```text
zuni ask [OPTIONS] PROMPT...
```

### Options

| Option | Description |
|--------|-------------|
| `--no-search` | Skip the agent/tool workflow and ask the model directly |
| `-n, --results INTEGER` | Maximum number of search results to use, from 1 to 10; default: 5 |

The prompt can contain multiple shell arguments. Zuni joins them into one question.

### Examples

=== "Research"

    ```bash
    zuni ask "What are the latest changes in Python?"
    zuni ask "Compare HTTP/1.1 and HTTP/2"
    ```

=== "Direct model"

    ```bash
    zuni ask --no-search "Explain recursion"
    zuni ask --no-search "Write a Python function that reverses a string"
    ```

=== "Control result count"

    ```bash
    zuni ask -n 3 "What is quantum computing?"
    zuni ask --results 8 "Compare current Linux distributions"
    ```

### How a researched question works

1. Zuni loads the system prompt and configuration.
2. The LLM receives the question plus the available tool definitions.
3. The model may call `web_search`.
4. Zuni runs the requested tool and sends the result back to the model.
5. The model may call `extract_markdown` to read a specific page.
6. The agent repeats the tool loop until the model answers or the step budget is reached.
7. Zuni renders the Markdown answer.
8. Cited sources are printed below the answer.

If the selected model does not support tool calling, Zuni falls back to a simpler flow: search first, then send the collected sources to the model.

### Sources

When web research is used, Zuni numbers sources:

```text
[1] Source title
URL: https://example.com/...
Source content...

[2] Another source
URL: https://example.org/...
Source content...
```

The model can cite them as `[1]`, `[2]`, etc. Zuni then prints the cited sources at the bottom of the response.

### Quoting tips

Quote questions containing shell characters:

```bash
zuni ask 'What does $PATH do?'
zuni ask "What is Python's GIL?"
```

### Save an answer

```bash
zuni ask "List five Linux commands" > answer.txt
```

Terminal Markdown styling is not preserved in redirected output.

### Alias

```bash
alias z='zuni ask'
z "What is a mutex?"
```

---

## `zuni config`

Interactively saves configuration:

```bash
zuni config
```

See [Configuration](../getting-started/configuration.md) for details.

---

## Help

```bash
zuni --help
zuni ask --help
zuni config --help
```