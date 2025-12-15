from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_FILE = "data.db"

def init_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        conn.execute('CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)')
        conn.close()

@app.route('/items', methods=['GET', 'POST'])
def items():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if request.method ==
