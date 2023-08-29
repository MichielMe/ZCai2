import os
from dotenv import load_dotenv
from currents_api import fetch_latest_news  # Your existing function for fetching news
from openai_api import generate_tweet  # Your existing function for generating tweets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()


def send_email(subject, content, to_email):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = os.getenv('GMAIL_EMAIL')
    msg['To'] = to_email

    # Plain text part (optional)
    text_part = MIMEText(content, 'plain')
    msg.attach(text_part)

    # HTML part
    html_part = MIMEText(content, 'html')
    msg.attach(html_part)

    # Connect to Gmail's SMTP server
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

    # Fetch the latest news
    news_data = fetch_latest_news(currents_api_key, limit=5)

    if news_data is None:
        print("Failed to fetch news data.")
        return

    news_titles = ' '.join([article['title'] for article in news_data])

    # Generate HTML-formatted summary using GPT-3.5 Turbo
    summary = generate_tweet(openai_api_key, news_data)
    # Send the summary via email
    send_email("Today's Trending News Summary", summary, email_to)


if __name__ == "__main__":
    main()
