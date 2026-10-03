# Commands

Zuni keeps its command-line interface small:

```bash
zuni [COMMAND] [ARGUMENTS]
```

| Command | Purpose |
|---------|---------|
| `zuni ask` | Ask a question, with optional web research |
| `zuni config` | Configure the API key, model, and base URL |
| `zuni --help` | Show command help |

---

## `zuni ask`

Ask a question directly from your terminal:

```bash
zuni ask "Explain how DNS works"
```

Web research is enabled by default. The model can choose to use Zuni's available tools before producing the answer.

### Syntax

```text
zuni ask [OPTIONS] PROMPT...
```

### Options

| Option | Description |
|--------|-------------|
| `--no-search` | Skip the agent and tools and ask the model directly |
| `-n, --results INTEGER` | Maximum number of search results, from 1 to 10; default: 5 |

If the prompt contains multiple shell arguments, Zuni joins them into one question.

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

=== "Choose result count"

    ```bash
    zuni ask -n 3 "What is quantum computing?"
    zuni ask --results 8 "Compare current Linux distributions"
    ```

### Research flow

For a normal research request:

1. Zuni loads the configuration and system prompt.
2. The LLM receives the question and available tool definitions.
3. The model can call `web_search`.
4. Zuni runs the requested tool and returns its result to the model.
5. The model can call `extract_markdown` when it needs to read a page.
6. The agent repeats the tool loop until the model answers or the step limit is reached.
7. Zuni renders the answer as Markdown.
8. Zuni prints the relevant sources below the answer.

If the selected model cannot use tool calling, Zuni switches to a simpler search-first flow: it collects web results and sends them to the model in a normal request.

### Sources and citations

Web sources are assigned numbers:

```text
[1] Source title
URL: https://example.com/...

[2] Another source
URL: https://example.org/...
```

The model is instructed to cite these numbers inline, for example `[1]`. Zuni then prints the corresponding source URLs below the answer.

### Shell quoting

Quote prompts when they contain shell characters such as `$`:

```bash
zuni ask 'What does $PATH do?'
zuni ask "What is Python's GIL?"
```

### Save an answer

Redirect the terminal output to a file:

```bash
zuni ask "List five Linux commands" > answer.txt
```

Rich terminal formatting is not preserved in the redirected output.

### Alias

You can create a short shell alias:

```bash
alias z='zuni ask'
z "What is a mutex?"
```

---

## `zuni config`

Run the interactive configuration command:

```bash
zuni config
```

It asks for the API key, model ID, and base URL. See [Configuration](../getting-started/configuration.md) for the details.

---

## Help

Use the built-in help whenever you need the exact command syntax:

```bash
zuni --help
zuni ask --help
zuni config --help
```