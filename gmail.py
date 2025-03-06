from dotenv import load_dotenv
import os

# Load your specific env file (instead of default .env)
load_dotenv(dotenv_path="my_gmail.env")

# Access variables
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

print(f"Email Address: {email_address}")  # Just to verify it's loaded correctly