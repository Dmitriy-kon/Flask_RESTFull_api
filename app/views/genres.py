from flask_restx import Namespace, Resource

from app.dao import GenreDao
from app.dao import GenreSchema

genres_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


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
