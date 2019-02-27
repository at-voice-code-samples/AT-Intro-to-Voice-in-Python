import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    response = "It lives"
    return response

@app.route("/voice/say", methods=["GET", "POST"])
def say():
    response = '<?xml version="1.0"?>'
    response += "<Response>"
    response += '<Say voice="woman">Hi, '
    response += "Welcome to the Africas Talking Voice Service. You built a voice app!</Say>"
    response += "</Response>"
    return response

@app.route("/voice/play", methods=["GET", "POST"])
def play():
    response = '<?xml version="1.0"?>'
    response += "<Response>"
    response += '<Play url="https://s3.eu-west-2.amazonaws.com/at-voice-sample/play.mp3"/>'
    response += "</Response>"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"), debug=True)
