from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from tavily import TavilyClient
import os

class TavilyToolInput(BaseModel):
    query: str = Field(description="Search query for recent Pakistani legal updates and news")

class PakistaniLawWebSearchTool(BaseTool):
    name: str = "Pakistani Law Web Search"
    description: str = (
        "Search the web for recent Pakistani legal updates, amendments, court decisions, "
        "and news. Use this to supplement the law database with current information "
        "that may not be in the static documents."
    )

    args_schema: type[BaseModel] = TavilyToolInput

    def _run(self, query: str) -> str:
        client = TavilyClient(api_key=os.getenv("Tavily_API_KEY"))

        results = client.search(
            query = f"Paksitan law {query}",
            max_results=3,
            search_depth="basic"
        )

        output = ""
        for r in results.get("results",[]):
            output += f"Source: {r['url']}\n"
            output += f"{r['content']}\n\n"

        if not output:
            return "No recent web results found"
        
        return output