"""OpenAI-compatible tool definitions (works with OpenRouter too).

Pass ``TOOLS`` as the ``tools`` field of a /chat/completions request. The
model answers with ``tool_calls`` whose ``function.name`` matches one of the
names below; ``Toolbox.run`` executes them.
"""
from __future__ import annotations

from typing import Any

WEB_SEARCH: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "web_search",
        "description": (
            "Search the web for current or factual information. Returns "
            "numbered sources (title, URL, page text) that must be cited "
            "as [n] in the final answer."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Short, specific search query (2-8 words).",
                },
                "max_results": {
                    "type": "integer",
                    "description": "How many results to return (1-10).",
                    "minimum": 1,
                    "maximum": 10,
                },
            },
            "required": ["query"],
        },
    },
}

EXTRACT_MARKDOWN: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "extract_markdown",
        "description": (
            "Download one web page and return its main content as Markdown. "
            "Use it to read a specific URL, for example one from search "
            "results or one the user gave."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "Full http(s) URL of the page to read.",
                },
            },
            "required": ["url"],
        },
    },
}

TOOLS: list[dict[str, Any]] = [WEB_SEARCH, EXTRACT_MARKDOWN]
