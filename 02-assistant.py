import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit()":
        print("Goodbye!")
        break
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("Assistant: " + reply + "\n")
