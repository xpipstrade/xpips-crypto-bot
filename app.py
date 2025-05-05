from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        print(data)  # Vérifie les données reçues dans les logs
        return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
