import openai
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import argparse

load_dotenv()

openai.api_key = os.environ.get('OPENAI_API_KEY')

def download_webpage(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to get URL. Status code: {response.status_code}")
        return None
    else:
        return response.text

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()
    return " ".join(soup.stripped_strings)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download and write a blog post based on a webpage.')
    parser.add_argument('url', type=str, help='The URL of the webpage to download and write a blog post about')
    args = parser.parse_args()

    url = args.url
    downloaded_webpage = download_webpage(url)
    if downloaded_webpage:
        extracted_text = extract_text_from_html(downloaded_webpage)

        # Include a system role and assistant's first message to set the behavior
        conversation = [
            {"role": "system", "content": "You are a helpful assistant familiar with SEO and blogging."},
            {"role": "user", "content": f"Write a blog post based on this article: {extracted_text}"}
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0.5,
        )

        print(completion.choices[0].message.content)
