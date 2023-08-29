News Summarizer and Notifier
Overview
This Python project automatically fetches the latest trending news articles using the Currents API, summarizes them using OpenAI's GPT-3.5 Turbo, and then sends the summary via email. The email includes a sleek, modern HTML layout styled with inline CSS, featuring placeholders for images and links.

Requirements
Python 3.x
A Currents API key
An OpenAI API key
Gmail account for sending emails
Installation
Clone the repository.

bash
Copy code
git clone https://github.com/your-username/your-repository.git
Navigate into the project directory.

bash
Copy code
cd your-repository
Install the required Python packages.

bash
Copy code
pip install -r requirements.txt
Setup
Create a .env file in the project root directory to store your API credentials and other sensitive information.

makefile
Copy code
CURRENTS_API=your_currents_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
GMAIL_EMAIL=your_gmail_email_here
GMAIL_PASSWORD=your_gmail_password_here
RECIPIENT_EMAIL=recipient_email_here
Make sure to replace the placeholders with your actual API keys and email credentials.

Running the Project
Execute the main.py script to fetch, summarize, and send the news summary.

bash
Copy code
python main.py
Contributions
Contributions, issues, and feature requests are welcome!
