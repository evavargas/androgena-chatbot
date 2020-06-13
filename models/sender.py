from connection.database import Connection

conn = Connection()
Model = conn.model()


class SenderModel(Model):
    __table__ = "sender"
    __primary_key__ = "id_sender"
    __timestamps__ = False
    __connection__ = "postgres"

    __guarded__ = []

    __fillable__ = ["id_sender"]

    __casts__ = {
        "id_sender" : "str"
    }

    __hidden__ = []
