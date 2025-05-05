from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os

app = Flask(__name__)

TOKEN = "7893984645:AAHXUAU0nScgo4MB18zjCWeg6W28Kgvfqdc"

application = Application.builder().token(TOKEN).build()

@app.route('/')
def home():
    return 'Bot en ligne'

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return 'OK'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
