from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = 'mongodb://mongo_service:27017/'

@app.route('/')
def check_connection():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)

        client.server_info()
        return '<h1>✅ Succès : Flask s'a connecté à la MongoDB !</h1>'
    except Exception as e:
        return f'<h1>❌ Erreur : Conncexion avec échec, Exception: {e}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)