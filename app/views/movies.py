from app.api.api_dao.movies_dao import MoviesDao
from flask_restx import Namespace, Resource

movies_ns = Namespace('movies')


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
