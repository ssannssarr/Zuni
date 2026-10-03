"""Runs the tools the model asks for and tracks numbered sources."""
from __future__ import annotations

import json
from typing import Any

from zuni.errors import ZuniError
from zuni.search.search import fetch_page
from zuni.tools.extract_markdown import extract_markdown, page_title
from zuni.tools.web_search import Source, format_source, format_sources, web_search


class Toolbox:
    """Executes tool calls and keeps one global list of sources.

    Citation numbers stay unique even when the model calls several tools,
    because every source is registered here and numbered once, by URL.
    Tool failures never raise: they come back as ``"Error: ..."`` text so
    the model can recover or explain.
    """

    def __init__(self, max_results: int = 5) -> None:
        self.max_results = max_results
        self.sources: list[Source] = []

    def add(self, title: str, url: str, content: str) -> Source:
        """Register a source (or update an existing one with the same URL)."""
        for source in self.sources:
            if source.url == url:
                if len(content) > len(source.content):
                    source.content = content
                return source
        source = Source(len(self.sources) + 1, title or url, url, content)
        self.sources.append(source)
        return source

    @staticmethod
    def parse_arguments(raw: Any) -> dict[str, Any]:
        """Decode a tool call's ``arguments`` (a JSON string, or a dict).

        Raises:
            ValueError: If it is not a JSON object.
        """
        if raw is None or raw == "":
            return {}
        if isinstance(raw, dict):
            return raw
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("arguments must be a JSON object")
        return data

    async def run(self, name: str, args: dict[str, Any]) -> str:
        """Run one tool and return the text sent back to the model."""
        try:
            if name == "web_search":
                return await self._web_search(args)
            if name == "extract_markdown":
                return await self._extract_markdown(args)
            return f"Error: unknown tool '{name}'."
        except ZuniError as exc:
            return f"Error: {exc}"
        except Exception as exc:  # a tool bug must not kill the session
            return f"Error: {type(exc).__name__}: {exc}"

    async def _web_search(self, args: dict[str, Any]) -> str:
        query = str(args.get("query", "")).strip()
        if not query:
            return "Error: 'query' is required."
        try:
            count = int(args.get("max_results", self.max_results))
        except (TypeError, ValueError):
            count = self.max_results
        count = max(1, min(count, 10))

        found = await web_search(query, max_results=count)
        registered = [self.add(s.title, s.url, s.content) for s in found]
        return format_sources(registered)

    async def _extract_markdown(self, args: dict[str, Any]) -> str:
        url = str(args.get("url", "")).strip()
        if not url:
            return "Error: 'url' is required."
        html = await fetch_page(url)
        text = extract_markdown(html, max_chars=6000)
        if not text:
            return "Error: no readable text was found on that page."
        source = self.add(page_title(html, fallback=url), url, text)
        return format_source(source)
