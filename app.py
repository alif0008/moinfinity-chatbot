import os
import streamlit as st
from langchain_groq import ChatGroq
import streamlit.components.v1 as components

# Load the scraped website content
with open("moinfinity_content.txt", "r", encoding="utf-8") as file:
    website_content = file.read()

# Initialize Groq Chat
groq_chat = ChatGroq(
    groq_api_key=os.environ.get("GROQ_API_KEY"),
    model_name="llama3-70b-8192"
)

# Define the assistant prompt
ASSISTANT_PROMPT = f"""
Chatbot Role and Function

You are a customer service chatbot for Moinfinity Digital...
{website_content}
"""

# Streamlit app
st.set_page_config(layout="wide")

# Inject custom CSS for a background GIF
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

st.title("Moinfinity Digital Assistant")
st.write("Welcome! I’m here to assist you with questions about our products, services, shipping, returns, and more!")

# Create columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_question = st.text_input("Ask a question:", key="user_input")

    if st.button("Submit"):
        if user_question:
            full_prompt = ASSISTANT_PROMPT + f"\n\nUser Question: {user_question}"
            response = groq_chat.predict(text=full_prompt)
            st.session_state.chat_history.append({"human": user_question, "AI": response})

    for chat in reversed(st.session_state.chat_history):
        st.write(f"You: {chat['human']}")
        st.write(f"Assistant: {chat['AI']}")

with col2:
    # Payment option on the right
    stripe_button_html = """
    <style>
        .stripe-container {
            text-align: right;
            padding: 10px;
        }
        .stripe-container h3 {
            color: white;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
        }
    </style>
    <div class="stripe-container">
        <h2>SUBSCRIBE NOW</h2>
        <script async src="https://js.stripe.com/v3/buy-button.js"></script>
        <stripe-buy-button
          buy-button-id="buy_btn_1QlO9yHqbUcykh7jNSVhkjST"
          publishable-key="pk_test_51QlNuNHqbUcykh7jbUjhUwGcw8BZw6XF5phEkiOiCNZhvUJJd7ArVZXzkM3i7cj57BGQcj2H6knBxAPqJt4Ge3ay00kzOzuKqc">
        </stripe-buy-button>
    </div>
    """
    components.html(stripe_button_html, height=300)
