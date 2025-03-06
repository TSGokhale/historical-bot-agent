import smtplib
import random
import os

OTP_STORE = {}

def generate_otp(email):
    otp = str(random.randint(100000, 999999))
    OTP_STORE[email] = otp
    send_otp_email(email, otp)
    return otp

def send_otp_email(email, otp):
    sender_email = os.getenv("GMAIL_USER")
    sender_password = os.getenv("GMAIL_APP_PASSWORD")

    message = f"Subject: Your Verification Code\n\nYour OTP is: {otp}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message)

def verify_otp(email, user_otp):
    correct_otp = OTP_STORE.get(email)
    if correct_otp and user_otp == correct_otp:
        return True
    return False
