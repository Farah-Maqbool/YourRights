from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from yourrights.tools.rag_tool import PakistanRAGTool
from yourrights.tools.tavily_tool import PakistaniLawWebSearchTool

@CrewBase
class Yourrights():
    """Yourrights crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        self.rag_tool = PakistanRAGTool()
        self.web_tool = PakistaniLawWebSearchTool()

    @agent
    def situation_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['situation_analyzer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def law_retreiever(self) -> Agent:
        return Agent(
            config=self.agents_config['law_retriever'], # type: ignore[index]
            tools= [self.rag_tool, self.web_tool],
            verbose=True
        )
    
    @agent
    def rights_explainer(self) -> Agent:
        return Agent(
            config = self.agents_config["rights_explainer"],
            verbose=True
        )

    @task
    def analyze_situation(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_situation'], # type: ignore[index]
        )

    @task
    def retrieve_laws(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_laws'], # type: ignore[index]
        )
    
    @task
    def explain_rights(self) -> Agent:
        return Task(
            config=self.tasks_config['explain_rights']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Yourrights crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
