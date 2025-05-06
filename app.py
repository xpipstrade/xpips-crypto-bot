from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, CommandHandler

TOKEN = "7893984645:AAHXUAU0nScgo4MB18zjCWeg6W28Kgvfqdc"  # Remplace par ton vrai token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

# Commande de base pour tester que le bot fonctionne
def start(update, context):
    update.message.reply_text("Bienvenue ! Le bot fonctionne ✅")

# Route de base pour tester que l'app est vivante
@app.route('/')
def index():
    return 'Bot Telegram XPips en ligne ✅'

# Route Webhook que Telegram appellera (POST uniquement)
@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Initialisation du dispatcher pour gérer les commandes
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)
dispatcher.add_handler(CommandHandler('start', start))

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
