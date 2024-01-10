import streamlit as st
from openai import AzureOpenAI
from datetime import datetime

# Initialize Azure OpenAI client (replace with your actual values)
client = AzureOpenAI(
    azure_endpoint="https://sunhackathon31.openai.azure.com/",
    api_key="9a81322a075f48acb8b612d3e38f6bc1",
    api_version="2023-05-15"
)

def main():
    st.title("Chatbox with Azure OpenAI")

    # Initialize or retrieve conversation history from session state
    conversation_history = st.session_state.get("conversation_history", [])

    # Create a text input for user messages
    user_input = st.text_input("You:", "")

    # Check if the user has entered any message
    if st.button("Send") and user_input:
        # Append user message to conversation history
        conversation_history.append({
            "role": "user",
            "message": user_input,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # Call the OpenAI API to generate a response
        response = generate_openai_response(user_input)

        # Append AI response to conversation history
        conversation_history.append({
            "role": "ai",
            "message": response,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        # Display the conversation history
        display_conversation_history(conversation_history)

    # Save conversation history to session state
    st.session_state.conversation_history = conversation_history

    # Button to clear the conversation history
    if st.button("Clear Conversation"):
        st.session_state.conversation_history = []

def generate_openai_response(user_input):
    # Call the OpenAI API to generate a response
    response = client.complete_prompt(prompt=user_input, temperature=0.7, max_tokens=100)

    # Extract the generated text from the response
    generated_text = response["choices"][0]["text"].strip()

    return generated_text

def display_conversation_history(conversation_history):
    # Display the conversation history with timestamps
    for entry in conversation_history:
        st.text(f"{entry['timestamp']} - {entry['role'].capitalize()}: {entry['message']}")

if __name__ == "__main__":
    main()
