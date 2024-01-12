import streamlit as st
from openai import AzureOpenAI

# Replace with your provided Azure OpenAI credentials
azure_endpoint = "https://sunhackathon31.openai.azure.com/"
api_key = "9a81322a075f48acb8b612d3e38f6bc1"
api_version = "2023-05-15"

# Streamlit UI
st.title("Azure OpenAI Chatbox")

# User input for Kanji character
user_input = st.text_input("You:", "")

# Model selection dropdown
selected_model = st.selectbox("Select Model:", ["gpt-35-turbo", "gpt-35-turbo-16k", "text-embedding-ada-002"])

# Send message button
if st.button("Send"):
    if user_input:
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
            messages=[{"role": "user", "content": user_input}]
        )
        assistant_response = response.choices[0].message.content

        if assistant_response:
            st.write(f"Assistant: {assistant_response}")

# Clear chat history button
if st.button("Clear Chat"):
    st.text("Chat cleared.")
