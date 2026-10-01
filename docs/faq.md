# FAQ

## What is Zuni?

A small CLI that sends a question to an AI model and prints the answer in your terminal.

## Is it free?

Zuni is free and open source (MIT). Model usage depends on your provider. OpenRouter offers free models such as `openrouter/free`.

## Which providers work?

Any provider with an OpenAI-compatible `/chat/completions` endpoint: OpenRouter, OpenAI, local servers like Ollama, and more.

## Does Zuni store my questions?

No. Zuni only saves your configuration locally. Your question is sent to the provider you configured, so their privacy policy applies.

## Where is my API key stored?

In plain text at `~/.config/zuni/config.json`. Restrict access with `chmod 600`.

## Can I use it offline?

Yes, with a local model server such as Ollama. Set its URL as your base URL.

## Does it search the web?

Not yet. Web search is on the [roadmap](roadmap.md).

## Can I have a conversation with follow-ups?

Not yet. Each `zuni ask` is a separate question.

## How do I change the model?

```bash
zuni config
```

or edit `~/.config/zuni/config.json`.

## How can I help?

See [Contributing](development/contributing.md).
