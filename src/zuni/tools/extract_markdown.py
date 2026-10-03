"""Turn raw HTML into compact Markdown for the model (pure Python)."""
from __future__ import annotations

import re

from bs4 import BeautifulSoup

try:
    from markdownify import markdownify
except ImportError:  # pragma: no cover - only if the dependency is missing
    markdownify = None  # falls back to plain text below

# Tags that never contain useful article text.
NOISE_TAGS = [
    "script", "style", "noscript", "nav", "footer", "aside",
    "header", "form", "svg", "iframe", "button",
]  # fmt: skip


def extract_markdown(html: str, max_chars: int = 4000) -> str:
    """Convert an HTML page to cleaned, length-limited Markdown.

    Steps: drop noise tags, pick ``<article>`` / ``<main>`` / ``<body>``,
    convert with markdownify, collapse blank lines, then truncate.
    If markdownify is not installed, plain text is returned instead.

    Args:
        html: Raw page HTML.
        max_chars: Maximum length of the returned text.

    Returns:
        Markdown text, or an empty string if nothing readable was found.
    """
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(NOISE_TAGS):
        tag.decompose()

    root = soup.find("article") or soup.find("main") or soup.body or soup
    if markdownify is not None:
        text = markdownify(str(root), heading_style="ATX", strip=["img"])
    else:
        text = root.get_text("\n", strip=True)

    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    if len(text) > max_chars:
        text = text[:max_chars].rsplit(" ", 1)[0] + "…"
    return text


def page_title(html: str, fallback: str = "") -> str:
    """Return the page's ``<title>`` text, or ``fallback`` if it has none."""
    soup = BeautifulSoup(html, "html.parser")
    if soup.title and soup.title.get_text(strip=True):
        return " ".join(soup.title.get_text().split())
    return fallback
