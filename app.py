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
    
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        cursor.execute('INSERT INTO items (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Item added successfully"}), 201
    
    elif request.method == 'GET':
        cursor.execute('SELECT * FROM items')
        rows = cursor.fetchall()
        conn.close()
        items_list = [{"id": row[0], "name": row[1]} for row in rows]
        return jsonify(items_list), 200

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Python Web App with SQLite!"}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)