from flask import Blueprint

bp_flask = Blueprint('api', __name__)

from . import dog_app