from flask import Flask
from flask_socketio import SocketIO
from flask_socketio import emit, join_room, leave_room
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
print(os.path.dirname(__file__))
from Share import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
