# proposal_crew/crew.py

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from crewai.llm import LLM
from .agents import create_agents
from .tasks import create_tasks

def run_proposal_crew(company_name: str, company_description: str = None):
    """
    Initializes and runs the proposal generation crew for a given company.
    """
    load_dotenv()
    
    os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")

    # Initializing the LLM
    llm = LLM(
        model="gemini/gemini-2.0-flash",
        api_key=google_api_key,
    )
    
    # Create agents and tasks
    agents = create_agents(llm)
    tasks = create_tasks(*agents, company_name, company_description)
    
    # Assemble and run the crew
    company_crew = Crew(
        agents=list(agents),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    result = company_crew.kickoff()
    
    # Clean the result
    cleaned_result = str(result).strip()
    if cleaned_result.startswith("```markdown"):
        cleaned_result = cleaned_result[11:].strip()
        cleaned_result = cleaned_result[:-3].strip()
    elif cleaned_result.startswith("```"):
        cleaned_result = cleaned_result[3:].strip()
        cleaned_result = cleaned_result[:-3].strip()
        
    return cleaned_result