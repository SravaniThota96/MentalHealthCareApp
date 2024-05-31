import os


from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_message(to: str, message: str) -> None:
    result = client.messages.create(
        from_= 'whatsapp:+14155238886',
        body=message,
        to=to
    )
