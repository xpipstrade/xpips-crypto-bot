
import requests
import os
from flask import Flask, request

app = Flask(__name__)

TOKEN = "7893984645:AAHXUAU0nScgo4MB18zjCWeg6W28Kgvfqdc"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", {}).get("text", "")
    chat_id = data.get("message", {}).get("chat", {}).get("id", "")
    if chat_id and message:
        send_message(chat_id, f"Hello from the bot: {message}")
    return {'status': 'ok'}, 200

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    requests.get(URL, params=params)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
