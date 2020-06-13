import os, requests, random, json
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class MessageController:
    def send_response(self,data,app):
        m_lists = ['Hola','Adios','Que tal?','Papelón']

        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        message_id = messaging_event["message"]["mid"]  
                        message_text = messaging_event["message"]["text"]
                        time = messaging_event["timestamp"]
        

        message_data = {
            "sender_id" : sender_id,
            "message_id" : message_id,
            "message_text" : message_text,
            "time" : time   
        }

        self.create(message_data)

        response = requests.post("https://graph.facebook.com/v2.6/me/messages",

        params={"access_token": os.getenv('PAGE_ACCESS_TOKEN')},

        headers={"Content-Type": "application/json"},

        data=json.dumps({
        "recipient": {"id": sender_id},
        "message": {"text": random.choice(m_lists)}
    }))

    def create(self,data):
       # sender = Sender.first_or_create(id_sender='John')
       print(data)
       #message = Messages.create(id_sender=data["sender_id"],id_message=data["sender_id"],time=data["sender_id"],text=data["message_text"])
