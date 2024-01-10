import os
import streamlit as st
from openai import AzureOpenAI

st.title("Chatbox with Azure OpenAI")

# Initialize AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("https://sunhackathon31.openai.azure.com/"),
    api_key=os.getenv("9a81322a075f48acb8b612d3e38f6bc1"),
    api_version="2023-05-15"
)

# Function to generate AI response
def generate_response(messages):
    response = client.chat.completions.create(
        model="GPT35TURBO",
        messages=messages
    )
    return response.choices[0].message.content

# Main Streamlit app
if __name__ == "__main__":
    messages = []

    while True:
        user_input = st.text_input("You:", key="user_input")
        if user_input:
            messages.append({"role": "user", "content": user_input})

            # Generate AI response
            assistant_response = generate_response(messages)
            messages.append({"role": "assistant", "content": assistant_response})

            # Display conversation in the chatbox
            for message in messages:
                if message["role"] == "user":
                    st.text_input("You:", message["content"], key=f"user_{len(messages)}")
                elif message["role"] == "assistant":
                    st.text_input("Assistant:", message["content"], key=f"assistant_{len(messages)}")

            # Clear user input after processing
            st.text_input("You:", key="user_input", value="")

        st.sleep(1)  # Sleep for a second to control the rate of requests
