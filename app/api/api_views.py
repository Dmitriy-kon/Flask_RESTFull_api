from flask import Blueprint
from flask_restx import Namespace, Resource

from app.api.api_dao.directors_dao import DirectorDao
from app.api.api_dao.genre_dao import GenreDao

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

directors_ns = Namespace('directors')
genres_ns = Namespace('genres')





@directors_ns.route('/')
class DirectorsView(Resource):
    directordao = DirectorDao()

    def get(self):
        directors = self.directordao.get_all()
        return directors

    def post(self):
        return self.directordao.post()


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    directordao = DirectorDao()

    def get(self, uid):
        directors = self.directordao.get_one(uid)
        return directors

    def put(self, uid):
        return self.directordao.put(uid)

    def delete(self, uid):
        return self.directordao.delete(uid)


@genres_ns.route('/')
class GenresView(Resource):
    genre_dao = GenreDao()

    def get(self):
        return self.genre_dao.get_all()

    def post(self):
        return self.genre_dao.post()


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    genre_dao = GenreDao()

    def get(self, uid):
        return self.genre_dao.get_one(uid)

    def put(self, uid):
        return self.genre_dao.put(uid)

    def delete(self, uid):
        return self.genre_dao.delete(uid)
