# Zuni

**Zuni** is a terminal research assistant that combines an OpenAI-compatible LLM with web search and source citations.

## Features

- Ask questions from the terminal
- Search the web automatically
- Extract readable page content for the model
- Return answers with source citations
- Use any compatible OpenAI-style API endpoint

## Installation

Requires Python 3.11 or newer.

Using `uv`:

```bash
uv tool install ssannssar.zuni
```

Or install into an environment:

```bash
uv add ssannssar.zuni
```

## Configuration

Set your API key:

```bash
zuni config --api-key YOUR_API_KEY
```

You can also configure the model and API base URL:

```bash
zuni config --model YOUR_MODEL --base-url YOUR_BASE_URL
```

Environment variables are supported too:

```bash
export ZUNI_API_KEY="YOUR_API_KEY"
export ZUNI_BASE_URL="https://your-provider.example/v1"
```

## Usage

Ask a question:

```bash
zuni ask "What is quantum computing?"
```

Skip web search:

```bash
zuni ask --no-search "Explain recursion"
```

Control the number of search results:

```bash
zuni ask -n 3 "Latest developments in Python"
```

See all commands and options:

```bash
zuni --help
zuni ask --help
```

## Documentation

Full documentation is available at:

https://ssannssarr.github.io/Zuni/

## Development

Clone the repository and install the project with its development dependencies:

```bash
git clone https://github.com/ssannssarr/Zuni.git
cd Zuni
uv sync
```

Run the CLI from the project environment:

```bash
uv run zuni --help
```

## License

Zuni is released under the MIT License. See [LICENSE](LICENSE).
