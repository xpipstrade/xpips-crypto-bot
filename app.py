from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, ContextTypes, filters
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "7893984645:AAHXUAU0nScgo4MB18zjCWeg6W28Kgvfqdc"   # Remplace par ton vrai token
bot = Bot(token=TOKEN)

app = Flask(__name__)

# Crée le dispatcher avec un worker pour les callbacks
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=1)

# Commande /start
def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text("Bot en ligne ✅")

# Réponse automatique
def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(f"Tu as dit : {update.message.text}")

# Enregistre les handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Point d'entrée Webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK', 200

# Page d’accueil simple
@app.route('/', methods=['GET'])
def index():
    return "Bot actif !", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
