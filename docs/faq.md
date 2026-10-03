# FAQ

## What is Zuni?

Zuni is a command-line AI research assistant. It sends questions to an OpenAI-compatible model and can use web-search tools to gather information before producing an answer.

## Does Zuni search the web?

Yes. Web research is enabled by default for `zuni ask`. The model can call `web_search` to search DuckDuckGo and `extract_markdown` to read a selected public page.

Use `--no-search` when you want to bypass the research workflow.

## Does every model support tool calling?

No. Tool calling depends on the model and provider.

If the first tool-enabled request fails, Zuni falls back to a simpler workflow:

```text
search the web → collect sources → send the sources to the model
```

## Is Zuni free?

The Zuni software is open source under the MIT License. Your model provider may charge for API usage, depending on the provider and model you choose.

## Which providers work?

Zuni targets providers that expose an OpenAI-compatible `POST /chat/completions` endpoint.

Tool calling also requires support for the `tools` request format.

## Does Zuni store my questions?

Zuni stores configuration locally and does not implement a server-side conversation database.

Requests sent to hosted model or web services are handled according to those services' own privacy policies.

## Where is my API key stored?

By default, a key entered through `zuni config` is stored at:

```text
~/.config/zuni/config.json
```

You can override it with `ZUNI_API_KEY`.

Protect the configuration file and never commit it to Git.

## Can I use a local model?

Yes, if the local model server exposes an OpenAI-compatible chat-completions endpoint.

For example:

```text
http://localhost:11434/v1
```

Use `--no-search` if you do not want Zuni to access the web.

## Can I use Zuni offline?

The direct LLM path can work without internet access when the configured model server is reachable locally.

Web research requires network access.

## How does citation work?

Zuni assigns numbers to collected sources:

```text
[1] First source
[2] Second source
```

The model is instructed to use those numbers for inline citations. Zuni then prints the corresponding source URLs below the answer.

## How do I control the number of search results?

Use the `-n` or `--results` option:

```bash
zuni ask -n 3 "Your question"
```

The allowed range is 1 to 10, with 5 as the default.

## How do I change the model?

Run:

```bash
zuni config
```

You can also edit:

```text
~/.config/zuni/config.json
```

The base URL can be overridden with `ZUNI_BASE_URL`.

## Where can I contribute?

See [Contributing](development/contributing.md) for the development workflow and contribution guidelines.