import os
from crewai import Agent, Task, Crew

# Groq Configuration
os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama3-8b-8192'
os.environ["OPENAI_API_KEY"] = 'YOUR_GROQ_API'
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.7,
    model="llama3-8b-8192",  # Make sure this matches Groq's model
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["OPENAI_API_KEY"]
)

def generate_title(life_story_summary: str) -> str:
    agent = Agent(
        role="Title Creator",
        goal="Create a captivating and relevant book title",
        backstory=" You are Expert and a professional book titling expert. You craft emotionally resonant and impactful titles.",
        verbose=False,
        allow_delegation=False,
        llm=llm 
    )
    

    task = Task(
        description=f"Based on the following summary of a life story, generate a compelling book title:\n\n{life_story_summary}",
        expected_output="A single sentence title",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False
    )

    result = crew.kickoff()
    return result
