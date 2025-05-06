from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

TOKEN = '7893984645:AAHXUAU0nScgo4MB18zjCWeg6W28Kgvfqdc'  # Remplace par ton token Telegram réel

app = Flask(__name__)
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)

# Commande /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot en ligne ✅")

# Répète les messages texte
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tu as dit : {update.message.text}")

# Ajoute les handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Route webhook : accepte uniquement POST
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Route racine pour test GET
@app.route('/', methods=['GET'])
def index():
    return 'Bot Xpips actif !'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


