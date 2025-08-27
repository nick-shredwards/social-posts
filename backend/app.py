
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Get up to 20 recent messages for the feed
@app.route('/api/messages', methods=['GET'])
def get_messages():
    conn = get_db_connection()
    messages = conn.execute('''
        SELECT messages.id, messages.message, messages.user_id, profiles.name as username
        FROM messages
        JOIN profiles ON messages.user_id = profiles.id
        ORDER BY messages.id DESC
        LIMIT 20
    ''').fetchall()
    conn.close()
    return jsonify([dict(row) for row in messages])

# Add a new message
@app.route('/api/messages', methods=['POST'])
def add_message():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO messages (user_id, message) VALUES (?, ?)', (data['user_id'], data['message']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Message added'}), 201

@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    conn = get_db_connection()
    profiles = conn.execute('SELECT * FROM profiles').fetchall()
    conn.close()
    return jsonify([dict(row) for row in profiles])

@app.route('/api/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return jsonify([dict(row) for row in posts])

@app.route('/api/profiles', methods=['POST'])
def add_profile():
    data = request.get_json()
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO profiles (name, password) VALUES (?, ?)', (data['name'], data['password']))
        conn.commit()
        result = {'status': 'Profile added'}
        status = 201
    except sqlite3.IntegrityError:
        result = {'error': 'Username already exists'}
        status = 400
    conn.close()
    return jsonify(result), status

# Register endpoint
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    conn = get_db_connection()
    try:
        cursor = conn.execute('INSERT INTO profiles (name, password) VALUES (?, ?)', (data['name'], data['password']))
        conn.commit()
        user_id = cursor.lastrowid
        result = {'status': 'Profile registered', 'user_id': user_id, 'username': data['name']}
        status = 201
    except sqlite3.IntegrityError:
        result = {'error': 'Username already exists'}
        status = 400
    conn.close()
    return jsonify(result), status

# Login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM profiles WHERE name = ?', (data['name'],)).fetchone()
    conn.close()
    if user and user['password'] == data['password']:
        return jsonify({'status': 'Login successful', 'user_id': user['id'], 'username': user['name']}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (user_id, content) VALUES (?, ?)', (data['user_id'], data['content']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Post added'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
