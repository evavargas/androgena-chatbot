import os
import requests
import random
import json
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class MessageController:
    def send_response(self,data,app):
        m_lists = ['Hola','Adios','Que tal?']

        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        recipient_id = messaging_event["recipient"]["id"]  
                        message_text = messaging_event["message"]["text"] 
        
        print(sender_id)


        response = requests.post("https://graph.facebook.com/v2.6/me/messages",

        params={"access_token": os.getenv('PAGE_ACCESS_TOKEN')},

        headers={"Content-Type": "application/json"},

        data=json.dumps({
        "recipient": {"id": sender_id},
        "message": {"text": random.choice(m_lists)}
    }))
