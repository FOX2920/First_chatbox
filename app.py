import streamlit as st
from openai import AzureOpenAI

# Replace with your provided Azure OpenAI credentials
azure_endpoint = "https://sunhackathon31.openai.azure.com/"
api_key = "9a81322a075f48acb8b612d3e38f6bc1"
api_version = "2023-05-15"

# Streamlit UI
st.title("Azure OpenAI Chatbox")

# User input
user_input = st.text_input("You:", "")

# Model selection dropdown
selected_model = st.selectbox("Select Model:", ["gpt-35-turbo", "gpt-35-turbo-16k", "text-embedding-ada-002"])

# Clear chat history button
if st.button("Clear Chat"):
    messages = []
else:
    messages = st.session_state.get("messages", [])

# Send message button
if st.button("Send"):
    if user_input:
        messages.append({"role": "user", "content": user_input})
        client = AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            api_version=api_version
        )
        
        # Choose the appropriate model based on user selection
        if selected_model == "gpt-35-turbo":
            model_name = "GPT35TURBO"
        elif selected_model == "gpt-35-turbo-16k":
            model_name = "GPT35TURBO16K"
        elif selected_model == "text-embedding-ada-002":
            model_name = "ADA"

        # Function to interact with the OpenAI chat model
        response = client.chat.completions.create(
            model=model_name,
            messages=messages
        )
        assistant_response = response.choices[0].message.content

        if assistant_response:
            messages.append({"role": "assistant", "content": assistant_response})

        # Save messages to session state
        st.session_state.messages = messages

# Display chat history
for message in messages:
    role = message["role"]
    content = message["content"]
    if role == "user":
        st.text(f"You: {content}")
    elif role == "assistant":
        st.write(f"Assistant: {content}")
