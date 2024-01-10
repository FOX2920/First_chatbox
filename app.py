import streamlit as st
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://sunhackathon31.openai.azure.com/",
    api_key="9a81322a075f48acb8b612d3e38f6bc1",
    api_version="2023-05-15"
)

# Function to interact with the OpenAI chat model
def generate_openai_response(messages):
    response = client.chat.completions.create(
        model="GPT35TURBO",
        messages=messages
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("Azure OpenAI Chatbox")

messages = []

while True:
    user_input = st.text_input("You:", "")
    if user_input:
        messages.append({"role": "user", "content": user_input})
        assistant_response = generate_openai_response(messages)
        messages.append({"role": "assistant", "content": assistant_response})
        st.text("Assistant: " + assistant_response)
