from flask import Flask
from flask_socketio import SocketIO
from cryptography.fernet import Fernet
import os

# Initialize the Flask application and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Your encryption key
secret_key = "YOUR_SECRET_KEY"  # Replace with your actual secret key
fernet = Fernet(secret_key)

# Basic route to check if it's working
@app.route('/')
def index():
    return "SecureChat App is Running"

# Starting the server with Gunicorn for production
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
