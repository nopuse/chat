from flask import Blueprint

site_blueprint = Blueprint('site_blueprint', __name__, template_folder='templates', static_folder='static')

from .main import routes
