import openai
import gradio
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = [{"role": "system", "content": "You are a AI asistant who specializes in building Youtube channels and is an expert in digital marketing."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Your You Tube Channel Assistant", description = "You are a AI asistant who specializes in building Youtube channels and is an expert in digital marketing.")

demo.launch(share=True)