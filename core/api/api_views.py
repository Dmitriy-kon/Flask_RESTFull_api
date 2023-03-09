from flask import Blueprint, request
from flask_restx import Api, Resource
from flask_restx.representations import output_json

from core.api.api_dao.movies_dao import MoviesDao
from core.api.api_dao.directors_dao import DirectorDao
from core.api.api_dao.genre_dao import GenreDao

from core.models.model import db, Movie, Genre, Director, MovieSchema, GenreSchema, DirectorSchema

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_blueprint)
api.representations = {'application/json; charset=utf-8': output_json}

movies_ns = api.namespace('movies')
directors_ns = api.namespace('directors')
genres_ns = api.namespace('genres')


@movies_ns.route('/')
class MoviesView(Resource):
    moviesdao = MoviesDao()

    def get(self):
        movies = self.moviesdao.get_all()
        return movies


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    moviesdao = MoviesDao()

    def get(self, uid):
        movie = self.moviesdao.get_one(uid)
        return movie


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