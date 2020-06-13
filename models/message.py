from connection.database import Connection

conn = Connection()
Model = conn.model()


class MessageModel(Model):
    __table__ = "messages"
    __primary_key__ = "id_message"
    __timestamps__ = True
    __connection__ = "postgres"

    __guarded__ = [
        "id_message",
    ]

    __fillable__ = ["id_sender", "time", "text"]
    __casts__ = {"id_sender": "str", "time": "str", "text": "str"}

    __hidden__ = []
