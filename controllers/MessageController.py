import os, requests, random, json
from dotenv import load_dotenv
from pathlib import Path
from models.sender import SenderModel
from models.message import MessageModel

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class MessageController:
    def send_response(self, data, app):
        m_lists = [
            "Mensaje automatico",
            "Hola ¿Como podemos ayudarte?",
            "¿Que tal?",
            "Mensaje automatico II",
        ]

        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        message_id = messaging_event["message"]["mid"]
                        message_text = messaging_event["message"]["text"]
                        time = messaging_event["timestamp"]

        message_data = {
            "sender_id": sender_id,
            "message_id": message_id,
            "message_text": message_text,
            "time": time,
        }

        self.create(message_data)

        if message_data["message_text"].upper() == "CHROMATICA":
            self.music_search(message_data["message_text"])
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
        else:
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

    def create(self, data):
        sender = SenderModel.first_or_create(id_sender=data["sender_id"])
        message = MessageModel.create(
            id_sender=data["sender_id"],
            id_message=data["message_id"],
            time=data["time"],
            text=data["message_text"],
        )


    def music_search(self,data,app):
        list_tracks = ''
        payload = {'apikey': os.getenv("MUSICMATCH_TOKEN"), 'q_track': "CHROMATICA"}
        response = requests.get("http://api.musixmatch.com/ws/1.1/track.search",params=payload)
        response = dict(response.json())
        body = response.get("message").get("body")
        for tracks in body["track_list"]:
            list_tracks += (tracks["track"]["track_name"] + ' - ' + tracks["track"]["artist_name"] + "\n")

        return list_tracks


        #return response.json()
