from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'mysecretkey'

    from .chat_app import chat_blueprint
    from .site import site_blueprint

    app.register_blueprint(chat_blueprint)
    app.register_blueprint(site_blueprint)

    socketio.init_app(app)
    return app
