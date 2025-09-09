import streamlit as st
from src.llm import LLM
from src.config.config import DEFAULT_MODEL, DEFAULT_SYSTEM_PROMPT

# App title
st.set_page_config(page_title="NeoStats GenAI Chatbot", layout="wide")
st.title("🤖 NeoStats GenAI Chatbot")

# Sidebar
st.sidebar.header("⚙️ Settings")

# API Key input
api_key = st.sidebar.text_input("Enter GROQ API Key", type="password")

# Model selection
model = st.sidebar.selectbox(
    "Choose Model",
    ["llama-3.1-8b-instant", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"],
    index=0,
)

# Temperature
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.5)

# System Prompt
system_prompt = st.sidebar.text_area("System Prompt", DEFAULT_SYSTEM_PROMPT)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Show messages
for msg in st.session_state["messages"]:
    role, content = msg
    with st.chat_message(role):
        st.markdown(content)

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state["messages"].append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Initialize LLM
    if not api_key:
        st.error("⚠️ Please enter your GROQ API Key in the sidebar.")
    else:
        llm = LLM(api_key=api_key, model=model, system_prompt=system_prompt)
        response = llm.chat(prompt, temperature=temperature)

        # Add bot message
        st.session_state["messages"].append(("assistant", response))
        with st.chat_message("assistant"):
            st.markdown(response)
