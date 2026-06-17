import os
import litellm
litellm.drop_params = True

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from yourrights.tools.rag_tool import PakistanRAGTool
from yourrights.tools.tavily_tool import PakistaniLawWebSearchTool

@CrewBase
class Yourrights():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.rag_tool = PakistanRAGTool()
        self.web_tool = PakistaniLawWebSearchTool()
        self.llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
        )

    @agent
    def situation_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['situation_analyzer'],
            llm=self.llm,
            verbose=True
        )

    @agent
    def law_retriever(self) -> Agent:
        return Agent(
            config=self.agents_config['law_retriever'],
            llm=self.llm,
            tools=[self.rag_tool, self.web_tool],
            verbose=True
        )

    @agent
    def rights_explainer(self) -> Agent:
        return Agent(
            config=self.agents_config['rights_explainer'],
            llm=self.llm,
            verbose=True
        )

    @task
    def analyze_situation(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_situation']
        )

    @task
    def retrieve_laws(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_laws']
        )

    @task
    def explain_rights(self) -> Task:
        return Task(
            config=self.tasks_config['explain_rights']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )