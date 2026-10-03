"""Web search tool: search, fetch the top pages, extract Markdown."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass

from zuni.search.search import ddg_search, fetch_page
from zuni.tools.extract_markdown import extract_markdown


@dataclass
class Source:
    """A numbered source the model can cite as ``[index]``."""

    index: int
    title: str
    url: str
    content: str  # page text if fetched, otherwise the search snippet


async def web_search(
    query: str,
    max_results: int = 5,
    fetch_top: int = 3,
    max_chars: int = 4000,
) -> list[Source]:
    """Search the web and enrich the top results with page text.

    Page fetching is best-effort: if a page fails to download or parse, that
    source simply keeps its search snippet.

    Raises:
        SearchError / NetworkError: If the search itself fails.
    """
    results = await ddg_search(query, max_results)
    sources = [
        Source(i, r.title, r.url, r.snippet)
        for i, r in enumerate(results, start=1)
    ]

    limit = asyncio.Semaphore(3)  # be polite: at most 3 downloads at once

    async def enrich(source: Source) -> None:
        async with limit:
            try:
                html = await fetch_page(source.url)
                text = extract_markdown(html, max_chars=max_chars)
            except Exception:  # best-effort; keep the snippet on any failure
                return
            if text:
                source.content = text

    await asyncio.gather(*(enrich(s) for s in sources[:fetch_top]))
    return sources


def format_source(source: Source) -> str:
    """Render one source as ``[n] Title / URL / text``."""
    return f"[{source.index}] {source.title}\nURL: {source.url}\n{source.content}"


def format_sources(sources: list[Source]) -> str:
    """Render sources as the numbered block placed in the prompt."""
    return "\n\n---\n\n".join(format_source(s) for s in sources)
