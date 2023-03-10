from app.api.api_dao.directors_dao import DirectorDao
from flask_restx import Namespace, Resource

directors_ns = Namespace('directors')


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
