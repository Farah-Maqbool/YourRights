from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from yourrights.rag_pipeline import ingest_laws, query_laws

ingest_laws()

class RAGToolInput(BaseModel):
    """Input schema for RAGTool."""
    query: str = Field(description="Legal query to search in Pakistani law documents")

class PakistanRAGTool(BaseTool):
    name: str = "Pakistani Law Search"
    description: str = (
        "Search through Pakistani legal documents including the Constitution, "
        "Pakistan Penal Code (PPC), and Code of Criminal Procedure (CrPC). "
        "Use this to find relevant laws, articles, and sections for any legal situation."
    )
    args_schema: Type[BaseModel] = RAGToolInput

    def _run(self, query: str) -> str:
        results = query_laws(query, n_results=5)
        if not results:
            return "No relevant laws found for this query."
        return results
