# product/__init__.py
from flask import Blueprint

product = Blueprint('product', __name__)

from . import routes
