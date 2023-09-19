import openai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = [{"role": "system", "content": "You are a AI assistant who specializes in building YouTube channels and is an expert in digital marketing."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

st.title("Your YouTube Channel Assistant")
st.write("You are a AI assistant who specializes in building YouTube channels and is an expert in digital marketing.")

user_input = st.text_input("You: ", "")
if st.button("Submit"):
    response = CustomChatGPT(user_input)
    st.write(f"AI Assistant: {response}")
