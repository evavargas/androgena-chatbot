import os, requests, random, json
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class MessageController:
<<<<<<< HEAD
    def send_response(self,data,app):
        m_lists = ['Hola','Adios','Que tal?','Papelón']
=======
    def send_response(self, data, app):
        m_lists = ["Hola", "Adios", "Que tal?"]
>>>>>>> 235f5f64a6dcd88de7484eb47139c2367d602652

        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
<<<<<<< HEAD
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
=======
                        recipient_id = messaging_event["recipient"]["id"]
                        message_text = messaging_event["message"]["text"]
>>>>>>> 235f5f64a6dcd88de7484eb47139c2367d602652

        print(sender_id)

        response = requests.post(
            "https://graph.facebook.com/v2.6/me/messages",
            params={"access_token": os.getenv("PAGE_ACCESS_TOKEN")},
            headers={"Content-Type": "application/json"},
            data=json.dumps(
                {
                    "recipient": {"id": sender_id},
                    "message": {"text": random.choice(m_lists)},
                }
            ),
        )

<<<<<<< HEAD
        data=json.dumps({
        "recipient": {"id": sender_id},
        "message": {"text": random.choice(m_lists)}
    }))

    def create(self,data):
       # sender = Sender.first_or_create(id_sender='John')
       print(data)
       #message = Messages.create(id_sender=data["sender_id"],id_message=data["sender_id"],time=data["sender_id"],text=data["message_text"])
=======
>>>>>>> 235f5f64a6dcd88de7484eb47139c2367d602652
