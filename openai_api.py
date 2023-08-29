import openai
from dotenv import load_dotenv
import os

load_dotenv()

def initialize_openai_api():
    openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_tweet(api_key, news_data):
    openai.api_key = api_key

    titles = ' '.join([article['title'] for article in news_data])
    links = ' '.join([article['url'] for article in news_data])

    messages = [
        {"role": "system", "content": "You are a professional journalist with a sense of humor, skilled in HTML and inline CSS styling."},
        {"role": "user", "content": f"Generate a humorous yet professional HTML-formatted summary newslettet of the following trending news titles: {titles}. and include these correspondending links: {links}. make it look modern and sleek. include funny flavour text. include a welcome header to greet Michiel and tell him here is his news."}
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
    )

    return completion.choices[0].message['content']