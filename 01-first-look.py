import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)