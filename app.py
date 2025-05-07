from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

TOKEN = "7893984645:AAHXUAU0nScgo4MB18zjCWeg6W28Kgvfqdc"
bot = Bot(token=TOKEN)

app = Flask(__name__)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

def start(update, context):
    update.message.reply_text("Bot en ligne ✅")

def echo(update, context):
    update.message.reply_text(f"Tu as dit : {update.message.text}")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

@app.route('/', methods=['GET'])
def index():
    return "Bot actif ✅", 200

if __name__ == '__main__':
    app.run(port=5000)
