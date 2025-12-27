import streamlit as st
from config import MODEL
from tutors.base_tutors import PythonClassBot
from Chatbot.engine import Chatbot
from dotenv import load_dotenv  
import os

load_dotenv( )
api_key = os.getenv('GROQ_API_KEY')

st.set_page_config(page_title="Python Class Bot")
st.title("python class tutor bot")
st.markdown("""This is an interactive chatbot that helps you learn Object OOP's concepts in Python""")
if not api_key:
    st.info("Please set the GROQ_API_KEY in the .env file to use the chatbot.")
    st.stop()

    #creating objects 
tutor = PythonClassBot()
chat_engine = Chatbot(api_key=api_key, model=MODEL)

    #intialize chat history
if "messages" not in st.session_state:
    chat_engine.add_system_message(tutor.get_system_prompt())
    chat_engine.add_assistant_message(tutor.greet())
    st.session_state.messages = chat_engine.messages

    #display chat messages
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

     #user input
if prompt := st.chat_input("Ask about Inheritance, Polymorphism, Encapsulayion, Abstraction..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    #streaming
    with st.chat_message("assistant"):
        response = st.write_stream(chat_engine.get_streaming_response(prompt))