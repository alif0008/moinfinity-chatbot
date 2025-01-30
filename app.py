import os
import streamlit as st
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

# Set page config to use wide mode
st.set_page_config(page_title="Chat with Groq!", layout="wide")

# Inject custom CSS for background
st.markdown(
    """
    <style>
    body {
        background: url('https://media.giphy.com/media/1H8sdPP3JDAR5iY0Yv/giphy.gif?cid=ecf05e47dniqeuvvympmmv9pn02venxkp53qtw9hmpfs83uk&ep=v1_gifs_search&rid=giphy.gif&ct=g') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and chatbot UI
st.title("Chat with Groq!")
st.write("Hello! I'm your friendly Groq chatbot. I can help answer your questions, provide information, or just chat. I'm also super fast! Let's start our conversation!")

# Memory for chat history
memory = ConversationBufferWindowMemory(k=10, memory_key="chat_history", return_messages=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
else:
    for message in st.session_state.chat_history:
        memory.save_context({'input': message['human']}, {'output': message['AI']})

# Initialize Groq chat object
groq_chat = ChatGroq(
    groq_api_key=os.environ.get("GROQ_API_KEY"),
    model_name='llama3-70b-8192'
)

# User input
user_question = st.text_input("Ask a question:")

if user_question:
    response = groq_chat.predict(text=user_question)
    message = {'human': user_question, 'AI': response}
    st.session_state.chat_history.append(message)
    st.write("Chatbot:", response)
