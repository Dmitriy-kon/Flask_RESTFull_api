from flask import Blueprint
from flask_restx import Namespace, Resource

from app.api.api_dao.directors_dao import DirectorDao
from app.api.api_dao.genre_dao import GenreDao

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

directors_ns = Namespace('directors')
genres_ns = Namespace('genres')








