from flask_restx import Namespace, Resource

from app.dao.movies_dao import MoviesDao
from app.dao import MovieSchema

from app.setup_bd import db

movies_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movies_ns.route('/')
class MoviesView(Resource):
    movies_dao = MoviesDao(db.session)

    def get(self):
        movies = self.moviesdao.get_all()
        return movies


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    movies_dao = MoviesDao(db.session)

    def get(self, uid):
        movie = self.moviesdao.get_one(uid)
        return movie
