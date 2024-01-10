import streamlit as st
from openai import AzureOpenAI

# Replace with your provided Azure OpenAI credentials
azure_endpoint = "https://sunhackathon31.openai.azure.com/"
api_key = "9a81322a075f48acb8b612d3e38f6bc1"
api_version = "2023-05-15"
model_name = "GPT35TURBO"  # You can choose one of the provided models

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version=api_version
)

# Function to interact with the OpenAI chat model
def generate_openai_response(messages):
    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("Azure OpenAI Chatbox")

messages = []

user_input = st.text_input("You:", "")
if st.button("Send"):
    if user_input:
        messages.append({"role": "user", "content": user_input})
        assistant_response = generate_openai_response(messages)
        messages.append({"role": "assistant", "content": assistant_response})
        st.text("Assistant: " + assistant_response)
