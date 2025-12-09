from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query):
    res = tavily.search(query, max_results=5)
    return res["results"]
