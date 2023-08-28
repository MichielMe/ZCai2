import os
from dotenv import load_dotenv
from currents_api import fetch_latest_news
from openai_api import generate_tweet
import smtplib
from email.message import EmailMessage

# Load environment variables
load_dotenv()

def send_email(subject, content, to_email):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = os.getenv('GMAIL_EMAIL')
    msg['To'] = to_email

    # Establish a secure session with Gmail's outgoing SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.getenv('GMAIL_EMAIL'), os.getenv('GMAIL_PASSWORD'))

    # Send email
    server.send_message(msg)
    server.quit()

def main():
    currents_api_key = os.getenv('CURRENTS_API')
    openai_api_key = os.getenv('OPENAI_API_KEY')
    email_to = os.getenv('RECIPIENT_EMAIL')

    # Fetch latest news
    news_data = fetch_latest_news(currents_api_key, limit=5)
    
    if news_data is None:
        print("Failed to fetch news data.")
        return

    news_titles = ' '.join([article['title'] for article in news_data])

    # Generate a summary using GPT-3.5 Turbo
    summary = generate_tweet(openai_api_key, news_titles)
    
    # Send the summary via email
    send_email("Today's Trending News Summary", summary, email_to)

if __name__ == "__main__":
    main()
