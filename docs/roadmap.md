# Roadmap

Zuni is developing from a small command-line question-answering tool into a compact terminal research assistant.

This roadmap describes direction rather than a fixed release schedule. Items can change as the project evolves.

## Available now

- [x] One-command questions with `zuni ask`
- [x] Interactive configuration with `zuni config`
- [x] OpenAI-compatible chat-completions support
- [x] Markdown rendering in the terminal
- [x] Asynchronous HTTP requests
- [x] Retry handling for temporary LLM API failures
- [x] Tool-calling agent
- [x] DuckDuckGo web search
- [x] Web-page extraction to Markdown
- [x] Numbered source tracking and citations
- [x] Fallback search flow for models without tool calling
- [x] Direct-answer mode with `--no-search`
- [x] First PyPI release (`0.1.0`)

## In progress

- [ ] Stronger validation of model-generated tool calls
- [ ] More robust URL and redirect safety
- [ ] Automated tests for configuration, tools, citations, and the agent loop
- [ ] Expanded documentation and API reference

## Planned

- [ ] Streaming responses
- [ ] Conversation mode
- [ ] Reading input from stdin
- [ ] Multiple saved configuration profiles
- [ ] Continuous integration

## Ideas

- Shell completions
- JSON and other structured output formats
- Additional research tools
- Local and offline-first workflows
- More provider-specific configuration options

!!! note
    The roadmap is intentionally flexible. Features may move, change, or be removed as Zuni's design develops.
