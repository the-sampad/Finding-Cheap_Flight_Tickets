import requests
from twilio.rest import Client
ACC_SID = 'ACefde644b08fb6bf4f550b4697a975378'
AUTH_TOKEN = '0972534771b69071dfa91ae8c1eaff77'
class Message:
    def __init__(self):
        self.client = Client(ACC_SID, AUTH_TOKEN)
        
    def send_message(self,message_text):
        
        msg = self.client.messages.create(
            body=message_text,
            from_='+12055513610',
            to='+917838238772'
        )
        print(msg.status)
