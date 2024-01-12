import streamlit as st
from openai import AzureOpenAI

# Replace with your provided Azure OpenAI credentials
azure_endpoint = "https://sunhackathon31.openai.azure.com/"
api_key = "9a81322a075f48acb8b612d3e38f6bc1"
api_version = "2023-05-15"

# Streamlit UI
st.title("Azure OpenAI Chatbox")

# User input for Kanji character
user_input = st.text_input("Kanji:", "")

# Model selection dropdown
selected_model = st.selectbox("Select Model:", ["gpt-35-turbo", "gpt-35-turbo-16k", "text-embedding-ada-002"])

# Generate a 10-word story with words related to the provided Kanji character
if st.button("Generate Story"):
    if user_input:
        client = AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            api_version=api_version
        )

        # Function to interact with the OpenAI chat model
        response = client.chat.completions.create(
            model=selected_model,
            messages=[{"role": "user", "content": f"Generate a 10-word story with the Kanji characters '{user_input}' in English"}]
        )
        assistant_response = response.choices[0].message.content

        if assistant_response:

            # Display the generated story
            st.write(f"Story: {assistant_response}")

            # Clear other elements in the UI
            st.text("")  # Add an empty text element to separate the story from other content

# Clear chat history button
if st.button("Clear Chat"):
    st.text("Chat cleared.")
