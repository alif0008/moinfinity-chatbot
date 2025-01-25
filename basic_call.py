import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "tell me a joker",
        }
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)