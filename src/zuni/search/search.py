"""Keyless web search (DuckDuckGo HTML) and page fetching.

Uses ``curl_cffi`` with Chrome impersonation when it is available, because
that is what keeps DuckDuckGo from blocking us. If it is missing, plain
``httpx`` is used instead and blocks become more likely.

Debug it on its own:  python -m zuni.search.search "your query"
"""
from __future__ import annotations

import asyncio
import ipaddress
from dataclasses import asdict, dataclass
from urllib.parse import parse_qs, urlparse

import httpx as ht
from bs4 import BeautifulSoup
from rich.console import Console

from zuni.errors import NetworkError, SearchError

try:
    from curl_cffi.requests import AsyncSession
    HAS_CURL = True
except ImportError:  # pragma: no cover - depends on platform
    HAS_CURL = False

try:
    from curl_cffi.requests.exceptions import RequestException as CurlError
except ImportError:  # pragma: no cover - depends on version
    CurlError = Exception  # type: ignore[misc,assignment]

console = Console()

DDG_URL = "https://html.duckduckgo.com/html/"
MAX_HTML_CHARS = 2_000_000

FALLBACK_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


@dataclass
class SearchResult:
    """One search hit."""

    title: str
    url: str
    snippet: str


def is_public_url(url: str) -> bool:
    """True for http(s) URLs that do not point at this machine or a LAN.

    Used before fetching URLs chosen by the model, so a poisoned web page
    cannot make Zuni read localhost or private-network addresses.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname:
        return False
    host = parsed.hostname.lower()
    if host == "localhost" or host.endswith(
        (".localhost", ".local", ".internal", ".lan")
    ):
        return False
    try:
        return ipaddress.ip_address(host).is_global
    except ValueError:
        return True  # a normal domain name


async def http_request(
    method: str,
    url: str,
    *,
    data: dict | None = None,
    timeout: float = 15.0,
) -> tuple[int, str]:
    """Make one HTTP request and return ``(status_code, body_text)``.

    This is the single place that talks to the web for scraping.

    Raises:
        NetworkError: The request could not be completed.
    """
    try:
        if HAS_CURL:
            async with AsyncSession(impersonate="chrome") as session:
                res = await session.request(
                    method,
                    url,
                    data=data,
                    timeout=timeout,
                    allow_redirects=True,
                )
                return res.status_code, res.text
        async with ht.AsyncClient(
            headers=FALLBACK_HEADERS,
            timeout=timeout,
            follow_redirects=True,
        ) as client:
            res = await client.request(method, url, data=data)
            return res.status_code, res.text
    except (CurlError, ht.HTTPError) as exc:
        host = urlparse(url).netloc or url
        raise NetworkError(f"Could not reach {host}: {exc}") from exc


def clean_result_url(href: str) -> str:
    """Unwrap DuckDuckGo's redirect link (``/l/?uddg=...``) to the real URL."""
    if href.startswith("//"):
        href = "https:" + href
    parsed = urlparse(href)
    if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):
        target = parse_qs(parsed.query).get("uddg")
        return target[0] if target else ""
    return href


async def ddg_search(
    query: str,
    max_results: int = 5
) -> list[SearchResult]:
    """Search DuckDuckGo and return up to ``max_results`` results.

    Raises:
        SearchError: Blocked, non-200 response, or nothing parseable.
        NetworkError: Could not reach DuckDuckGo.
    """
    status, html = await http_request("POST", DDG_URL, data={"q": query})

    if status in (202, 403, 429) or "anomaly" in html[:5000].lower():
        raise SearchError(
            "DuckDuckGo blocked the request (rate limit or CAPTCHA). "
            "Wait a minute and try again."
        )
    if status != 200:
        raise SearchError(f"DuckDuckGo returned HTTP {status}.")

    soup = BeautifulSoup(html, "html.parser")  # stdlib parser, no lxml
    results: list[SearchResult] = []
    for block in soup.select("div.result"):
        if "result--ad" in (block.get("class") or []):
            continue  # skip sponsored results
        link = block.select_one("a.result__a")
        if link is None:
            continue
        url = clean_result_url(str(link.get("href", "")))
        if not url.startswith("http"):
            continue
        snippet_tag = block.select_one(".result__snippet")
        results.append(
            SearchResult(
                title=link.get_text(" ", strip=True),
                url=url,
                snippet=(
                    snippet_tag.get_text(" ", strip=True)
                    if snippet_tag else ""
                ),
            )
        )
        if len(results) >= max_results:
            break

    if not results:
        raise SearchError(
            "No results could be read. The query may have no matches, or "
            "DuckDuckGo changed its page layout."
        )
    return results


async def fetch_page(url: str) -> str:
    """Download a page and return its HTML (capped at ~2 MB of text).

    Raises:
        SearchError: Local/private address, or the server sent an error.
        NetworkError: Could not reach the server.
    """
    if not is_public_url(url):
        raise SearchError(
            "Refusing to fetch a local, private or non-http(s) address."
        )
    status, html = await http_request("GET", url)
    if status >= 400:
        raise SearchError(f"{urlparse(url).netloc} returned HTTP {status}.")
    return html[:MAX_HTML_CHARS]


def main() -> None:
    """Command line debug helper: print raw search results as JSON."""
    import sys

    if len(sys.argv) < 2:
        console.print("Usage: python -m zuni.search.search 'your query'")
        sys.exit(1)
    results = asyncio.run(ddg_search(sys.argv[1], max_results=10))
    console.print_json(data=[asdict(r) for r in results])


if __name__ == "__main__":
    main()
