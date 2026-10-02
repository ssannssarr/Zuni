from bs4 import BeautifulSoup
from curl_cffi import requests as cffi
from rich.console import Console


console = Console()


def ddg_search(
        query: str,
        max_results: int = 5
) -> list[dict]:
    r = cffi.post(
        "https://html.duckduckgo.com/html/",
        data={"q": query},
        impersonate="chrome",
        timeout=10,
    )
    soup = BeautifulSoup(r.text, "html.parser")  # ← stdlib, no lxml
    results = []
    for a in soup.select("a.result__a")[:max_results]:
        snippet = a.find_parent("div")
        snip_el = snippet.find(
            "a", class_="result__snippet"
        ) if snippet else None
        results.append({
            "title": a.get_text(),
            "url": a.get("href"),
            "snippet": snip_el.get_text() if snip_el else "",
        })
    return results


def main():
    import sys
    query = sys.argv[1]
    res = ddg_search(
        query=query,
        max_results=10
    )
    console.print_json(data=res)


if __name__ == "__main__":
    main()
