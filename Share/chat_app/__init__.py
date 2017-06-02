from flask import Blueprint

chat_blueprint = Blueprint('chat_blueprint', __name__, template_folder='templates')

from .main import routes, events
