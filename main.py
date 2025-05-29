import os
from flask import Flask, jsonify

app = Flask(__name__)

# Конфигурация через переменные окружения
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'mydb')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')

@app.route('/')
def index():
    #Тут он возвращает информацию о базе данных в формате Json
    return jsonify(
        message="My name is Simon Kazantsev",
        database={
            "host": DB_HOST,
            "port": DB_PORT,
            "name": DB_NAME,
            "user": DB_USER,
            "password": DB_PASSWORD
        }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)