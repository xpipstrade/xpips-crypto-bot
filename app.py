from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

TOKEN = "7893984645:AAHXUAU0nScgo4MB18zjCWeg6W28Kgvfqdc"
bot = Bot(token=TOKEN)

app = Flask(__name__)

# Crée le dispatcher
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)

# Commande /start
def start(update: Update, context):
    update.message.reply_text("Bot en ligne ✅")

# Message texte
def echo(update: Update, context):
    update.message.reply_text(f"Tu as dit : {update.message.text}")

# Enregistre les handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK', 200

@app.route('/', methods=['GET'])
def index():
    return "Bot actif !", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
