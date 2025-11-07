import streamlit as st

def get_response(user_input):
    user_input = user_input.lower()
    if user_input == 'hello':
        return "Hello there!"
    elif user_input == 'how are you?':
        return "I'm just a program, but I'm doing great!"
    elif user_input == 'what is your name?':
        return "I'm a simple Python chatbot."
    elif user_input == 'bye':
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that."

st.title("Chatbot")

user_input = st.text_input("You: ", "")

if user_input:
    response = get_response(user_input)
    st.write(f"Bot: {response}")
