import os
from dotenv import load_dotenv
from pathlib import Path
from flask import request
from controllers.MessageController import MessageController

MessageController = MessageController()

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


def routes(app):
    @app.route("/", methods=["GET"])
    def verification():
        if request.args.get("hub.verify_token", "") == os.getenv("VERIFY_TOKEN"):
            print("Verified")
            return request.args.get("hub.challenge", "")
        else:
            print("Wrong token")
            return "Error, wrong validation token"

    @app.route("/", methods=["POST"])
    def handle_message():
        data = request.get_json()
        MessageController.send_response(data, app)
        return "ok"
