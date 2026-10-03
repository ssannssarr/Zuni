# Roadmap

Zuni is evolving from a small CLI question-answering tool into a compact terminal research assistant.

This roadmap describes the current direction. It is not a fixed release schedule.

## Available now

- [x] `zuni ask` for one-command questions
- [x] `zuni config` for API key, model, and base URL
- [x] OpenAI-compatible chat-completions support
- [x] Markdown rendering in the terminal
- [x] Async HTTP requests
- [x] Retry handling for temporary LLM API failures
- [x] Agent/tool-calling loop
- [x] DuckDuckGo web search
- [x] Web-page extraction to Markdown
- [x] Numbered source tracking and citations
- [x] Fallback search flow for models without tool calling
- [x] `--no-search` direct-answer mode

## In progress

- [ ] Stronger validation of model-generated tool calls
- [ ] More robust URL and redirect safety
- [ ] Automated tests for configuration, tools, citations, and the agent loop
- [ ] Better documentation and API reference

## Planned

- [ ] Streaming responses
- [ ] Conversation mode
- [ ] Reading input from stdin
- [ ] Multiple saved profiles
- [ ] CI pipeline
- [ ] PyPI release

## Ideas

- Shell completions
- JSON and other structured output modes
- Additional research tools
- Local/offline-first workflows
- More provider-specific configuration options

!!! note
    The roadmap can change as Zuni's architecture and goals evolve.