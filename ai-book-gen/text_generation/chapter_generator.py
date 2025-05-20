import os
from crewai import Agent, Task, Crew
import os

# Groq Configuration
os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama3-8b-8192'
os.environ["OPENAI_API_KEY"] = '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'
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.7,
    model="llama3-8b-8192",  # Make sure this matches Groq's model
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["OPENAI_API_KEY"]
)

def generate_chapters(life_events: list) -> list:
    agent = Agent(
        role="Chapter Planner",
        goal="Design a structured outline of book chapters based on life events",
        backstory="Specialist in storytelling and structuring autobiographical narratives",
        verbose=False,
        allow_delegation=False,
        llm=llm 
    )

    events_text = "\n".join(f"{i+1}. {event}" for i, event in enumerate(life_events))

    task = Task(
        description=f"Create a list of book chapters based on the following key life events:\n{events_text}",
        expected_output="List of just chapter titles with numbers",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False
    )

    result = crew.kickoff()
    return result
