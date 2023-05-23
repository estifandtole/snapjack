import streamlit as st
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right
placeholder = st.empty()
input_text = st.text_input("You: ","Hello, how are you?", key="input")

if input_text:
	placeholder = message(input_text, is_user=True)