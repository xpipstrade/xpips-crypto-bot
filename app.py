from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot XPIPS en ligne !"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Remplace ceci par ton code qui traite les requêtes Telegram
    return "Webhook reçu"

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot XPIPS en ligne !"

# Si tu as une autre route comme /webhook, laisse-la en dessous
# Exemple :
# @app.route("/webhook", methods=["POST"])
# def webhook():
#     ...

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
