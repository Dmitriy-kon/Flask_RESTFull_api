from flask import Blueprint, request
from flask_restx import Api, Resource
from flask_restx.representations import output_json

from core.api.api_dao.api_dao import MoviesDao
from core.models.model import db, Movie, Genre, Director, MovieSchema, GenreSchema, DirectorSchema

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_blueprint)
api.representations = {'application/json; charset=utf-8': output_json}

movie_ns = api.namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    moviesdao = MoviesDao()

    def get(self):
        movies = self.moviesdao.get_all()
        return movies, 200


@movie_ns.route('/<int:uid>')
class MoviesView(Resource):
    moviesdao = MoviesDao()

    def get(self, uid):
        movie = self.moviesdao.get_one(uid)
        return movie, 200
