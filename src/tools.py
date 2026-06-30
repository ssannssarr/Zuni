tools = [
	{
	  "type": "openrouter:datetime",
	  "parameters": {
	    "timezone": "Asia/Kolkata"
	  }
	},
	{
	    "type": "function",
	    "function": {
	        "name": "web_search",
	        "description": "Search the internet for real-time data, news, and current events.",
	        "parameters": {
	            "type": "object",
	            "properties": {
	                "query": {"type": "string", "description": "The exact web search string."}
	            },
	            "required": ["query"]
	        }
	    }
	}
]


import requests

def web_search(query: str, max_results: int = 5) -> str:
    """
    Queries a SearXNG metasearch instance and returns a compiled text chunk 
    of page titles, snippets, and source links for an LLM to read.
    """
    url = "http://localhost:8080/search"
    params = {
        "q": query,
        "format": "json",       # Crucial: Forces SearXNG to reply with parseable JSON data
        "pageno": 1,
        "safesearch": 1
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Parse out clean data for the LLM
        results = data.get("results", [])[:max_results]
        if not results:
            return "No web results found."
            
        compiled_text = []
        for res in results:
            title = res.get("title", "No Title")
            snippet = res.get("content", "No Snippet Provided")
            link = res.get("url", "")
            compiled_text.append(f"Title: {title}\nURL: {link}\nSnippet: {snippet}\n---")
            
        return "\n".join(compiled_text)
        
    except Exception as e:
        return f"Search execution failed: {str(e)}"




