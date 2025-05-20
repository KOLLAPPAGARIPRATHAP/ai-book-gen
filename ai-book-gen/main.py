import os
from crewai import Agent, Task, Crew

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

import streamlit as st
from text_generation.title_generator import generate_title
from text_generation.chapter_generator import generate_chapters
from text_generation.summary_to_script import convert_summary_to_script

st.set_page_config(page_title="Just-in-Time AI Book Creator", layout="wide")

st.title("📖 Just-in-Time AI Book Creator")
st.markdown("Generate a personalized book based on your life story using Groq's LLaMA 3 & CrewAI.")

with st.form("input_form"):
    st.subheader("Step 1: Describe Your Life Story")
    life_story = st.text_area("Enter a brief summary of your life story:", height=200)

    st.subheader("Step 2: List Key Life Events")
    events_input = st.text_area("Enter important life events (one per line):", height=200)

    submit = st.form_submit_button("Generate Book")

if submit and life_story and events_input:
    with st.spinner("Generating book title..."):
        title = generate_title(life_story)
        st.success("✅ Book Title Generated!")
        st.write(f"### 📘 {title}")

    events = [e.strip() for e in events_input.splitlines() if e.strip()]
    with st.spinner("Creating chapter outline..."):
        chapters = generate_chapters(events)
        st.success("✅ Chapters Generated!")
        st.markdown("### 🧾 Chapter List")
        st.markdown(chapters)

    st.subheader("📜 Chapter Narratives")
    chapter_list = [line.strip() for line in chapters.splitlines() if line.strip()]
    
    for i, chapter in enumerate(chapter_list):
        with st.spinner(f"Writing Chapter {i+1}..."):
            script = convert_summary_to_script(chapter_title=chapter, summary=life_story)
            st.markdown(f"#### ✍️ {chapter}")
            st.markdown(script)
