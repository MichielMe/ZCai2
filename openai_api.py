import openai
from dotenv import load_dotenv
import os

load_dotenv()

def initialize_openai_api():
    openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_tweet(api_key, prompt):
    openai.api_key = api_key

    messages = [
        {"role": "system", "content": "You are a proffesional journalist and a news summarizer assistant with a sense of humor."},
        {"role": "user", "content": f"Summarize the following trending news titles for me into one text: {prompt}"}
        ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return completion.choices[0].message['content']