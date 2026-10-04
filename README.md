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

Install the latest release from PyPI with `uv`:

```bash
uv tool install ssannssarr.zuni
```

Verify the installation:

```bash
zuni --help
```

## Configuration

Run the interactive configuration command:

```bash
zuni config
```

Zuni asks for your API key, model ID, and base URL.

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
