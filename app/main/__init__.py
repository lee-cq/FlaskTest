from flask import Blueprint
from . import views

main = Blueprint('main', __name__)

main.add_url_rule('/', endpoint='homepage', view_func=views.home)
