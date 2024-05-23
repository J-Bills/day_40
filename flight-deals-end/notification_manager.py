from twilio.rest import Client
import os

TWILIO_SID = os.environ['YOUR TWILIO ACCOUNT SID']
TWILIO_AUTH_TOKEN = [TWILIO_AUTH_TOKEN]
TWILIO_VIRTUAL_NUMBER = ['TWILIO_NUM']
TWILIO_VERIFIED_NUMBER = 'actual phone number'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
