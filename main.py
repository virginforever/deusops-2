import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Конфигурация через переменные окружения
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_NAME = os.environ.get('DB_NAME', 'mydb')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route('/')
def index():
    return health() 


@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1;')
        cur.close()
        conn.close()
        db_status = "ok"
    except Exception as e:
        db_status = "fail"
    
    overall_status = "ok" if db_status == "ok" else "fail"
    return jsonify(
        status=overall_status,
        database_status=db_status,
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