# Commands

```bash
zuni [COMMAND] [ARGUMENTS]
```

| Command | Purpose |
|---------|---------|
| `zuni ask` | Ask a question and read the answer in your terminal |
| `zuni config` | Save API key, model and base URL |
| `zuni --help` | Show all commands |

---

## `zuni ask`

Sends your question to the configured model and renders the reply as Markdown.

```bash
zuni ask "Explain how DNS works"
```

### Usage

```text
zuni ask PROMPT
```

| Argument | Required | Description |
|----------|----------|-------------|
| `PROMPT` | Yes | Your question, wrapped in quotes |

### What happens

1. The system prompt is loaded
2. Your question is added as the user message
3. The request goes to `POST {BASE_URL}/chat/completions`
4. The answer is printed with formatting (headings, lists, code blocks)

### Examples

=== "Learning"

    ```bash
    zuni ask "What is the difference between TCP and UDP?"
    zuni ask "Explain recursion like I am 12"
    ```

=== "Coding"

    ```bash
    zuni ask "Write a Python function to reverse a string"
    zuni ask "What does git rebase do?"
    ```

=== "Quick facts"

    ```bash
    zuni ask "Summarize the CAP theorem in 3 lines"
    zuni ask "Convert 72 F to Celsius"
    ```

### Quoting tips

```bash
# Good
zuni ask "What is Python's GIL?"

# Bad: the apostrophe breaks unquoted input
zuni ask What is Python's GIL?
```

Use single quotes if your question contains `$` or `!`:

```bash
zuni ask 'What does $PATH do?'
```

### Shell tricks

Pipe a file into your question:

```bash
zuni ask "Explain this code: $(cat main.py)"
```

Save an answer to a file (formatting will be plain text):

```bash
zuni ask "List 5 Linux commands" > answer.txt
```

Create a short alias:

```bash
alias z='zuni ask'
z "What is a mutex?"
```

---

## `zuni config`

Interactively saves your settings.

```bash
zuni config
```

You are asked for the API key, model ID and base URL. The result is written to `~/.config/zuni/config.json`.

See [Configuration](../getting-started/configuration.md) for all options.

---

## Help

```bash
zuni --help
zuni ask --help
zuni config --help
```
