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

def convert_summary_to_script(chapter_title: str, summary: str) -> str:
    agent = Agent(
        role="Narrative Writer",
        goal="Convert chapter summary into a detailed and emotional narrative script with subheadings and bold letters if needed",
        backstory="Skilled in transforming summaries into immersive storytelling content",
        verbose=False,
        allow_delegation=False,
        llm=llm 
    )

    task = Task(
        description=f"Convert the following summary into a well-written narrative script for the chapter titled '{chapter_title}':\n\n{summary}",
        expected_output="Detailed narrative with dialogue or descriptions as needed with subheadings and bold letters if needed",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False
    )

    result = crew.kickoff()
    return result
