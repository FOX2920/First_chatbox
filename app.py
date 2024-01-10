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

# User input
user_input = st.text_input("You:", "")

# Clear chat history button
if st.button("Clear Chat"):
    messages = []

if st.button("Send"):
    if user_input:
        messages.append({"role": "user", "content": user_input})
        assistant_response = generate_openai_response(messages)
        if assistant_response:
            messages.append({"role": "assistant", "content": assistant_response})

# Display chat history
for message in messages:
    role = message["role"]
    content = message["content"]
    if role == "user":
        st.text(f"You: {content}")
    elif role == "assistant":
        st.write(f"Assistant: {content}")
