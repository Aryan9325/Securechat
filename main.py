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
if __name__ == '__main__':
    # Run the app using gunicorn in production environment
    from gunicorn.app.base import BaseApplication
    from gunicorn.six import iteritems

    class FlaskGunicornApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.app = app
            super().__init__()

        def load(self):
            return self.app

        def load_config(self):
            for key, value in iteritems(self.options):
                self.cfg.set(key, value)

    options = {
        'bind': '0.0.0.0:5000',  # The host and port to bind the server to
    }
    FlaskGunicornApplication(app, options).run()

    
