from flask import Flask
from flask_socketio import SocketIO
from cryptography.fernet import Fernet
import os

# Initialize the Flask application and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Your encryption key
secret_key = "YOUR_SECRET_KEY"
fernet = Fernet(secret_key)

# Basic route to check if it's working
@app.route('/')
def index():
    return "SecureChat App is Running"

# Starting the server with Gunicorn for production
if __name__ == '__main__':
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
    
