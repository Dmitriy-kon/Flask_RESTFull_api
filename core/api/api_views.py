from flask import Blueprint, request
from flask_restx import Api, Resource
from flask_restx.representations import output_json

from core.api.api_dao.movies_dao import MoviesDao
from core.api.api_dao.directors_dao import DirectorDao


from core.models.model import db, Movie, Genre, Director, MovieSchema, GenreSchema, DirectorSchema

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_blueprint)
api.representations = {'application/json; charset=utf-8': output_json}

movies_ns = api.namespace('movies')
directors_ns = api.namespace('directors')


@movies_ns.route('/')
class MoviesView(Resource):
    moviesdao = MoviesDao()

    def get(self):
        movies = self.moviesdao.get_all()
        return movies, 200


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    moviesdao = MoviesDao()

    def get(self, uid):
        movie = self.moviesdao.get_one(uid)
        return movie, 200


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
