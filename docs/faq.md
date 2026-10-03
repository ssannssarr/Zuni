# FAQ

## What is Zuni?

Zuni is a command-line AI research assistant. It sends questions to an OpenAI-compatible model and can use web-search tools to gather information before producing an answer.

## Does Zuni search the web?

Yes. Web research is enabled by default for `zuni ask`. The model can use `web_search` to search DuckDuckGo and `extract_markdown` to read a specific public page.

Use `--no-search` to bypass the research workflow.

## Does every model support tool calling?

No. Tool calling depends on the model/provider. If the first tool-enabled request fails, Zuni falls back to a simpler search-first flow: search the web, collect sources, then send them to the model in a normal request.

## Is Zuni free?

The Zuni software is open source under the MIT License. Your model provider may charge for API usage.

## Which providers work?

Zuni targets providers with an OpenAI-compatible `POST /chat/completions` endpoint. Tool calling additionally requires support for the `tools` request format.

## Does Zuni store my questions?

Zuni stores its configuration locally and does not implement a server-side conversation database. Requests sent to hosted model or web services are subject to those services' privacy policies.

## Where is my API key stored?

By default, the key entered through `zuni config` is stored in:

```text
~/.config/zuni/config.json
```

You can override it with `ZUNI_API_KEY`. Protect the config file and never commit it.

## Can I use a local model?

Yes, if the local server exposes an OpenAI-compatible chat-completions endpoint. For example:

```text
http://localhost:11434/v1
```

Use `--no-search` if you do not want Zuni to access the web.

## Can I use Zuni offline?

The direct LLM path can work without internet when the configured model server is reachable locally. Web research requires network access.

## How does citation work?

Zuni assigns numbers to collected sources:

```text
[1] First source
[2] Second source
```

The model is instructed to cite those numbers inline. Zuni then prints the corresponding URLs below the answer.

## How do I control search results?

```bash
zuni ask -n 3 "Your question"
```

The allowed range is 1 to 10.

## How do I change the model?

Run `zuni config` or edit `~/.config/zuni/config.json`. You can also override the base URL with `ZUNI_BASE_URL`.

## Where can I contribute?

See [Contributing](development/contributing.md).