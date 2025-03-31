from flask import Flask, render_template
from flask_socketio import SocketIO, send
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Generate a secret key for encryption
SECRET_KEY = b'ctv1GpJD_gfZAxdFe8aKJwTi0fHDUjn-dbO6tdvQAfE='  # Replace with actual key
cipher = Fernet(SECRET_KEY)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(encrypted_msg):
    send(encrypted_msg)  # Forward encrypted message to all clients

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
    