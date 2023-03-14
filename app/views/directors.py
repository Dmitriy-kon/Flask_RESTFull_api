from app.container import director_service
from app.dao.models.directors import DirectorSchema

from flask_restx import Namespace, Resource, fields
from marshmallow import ValidationError
from flask import request

directors_ns = Namespace('directors')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()

# Director model for documentation
director_model = directors_ns.model("Director", {
    "id": fields.Integer(required=False, description="Director identification"),
    "name": fields.String(required=True, description="Director name")
})


@directors_ns.route('/')
class DirectorsView(Resource):
    @directors_ns.doc(description="Get directors",
                      params={
                          "id": "director id",
                          "name": "director name"
                      })
    @directors_ns.response(200, "Success", director_model)
    @directors_ns.response(404, "Not found")
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200

    @directors_ns.doc(description="add new director", body=director_model)
    @directors_ns.response(201, "Created")
    @directors_ns.response(400, "Validation Error")
    def post(self):
        try:
            data = director_schema.load(request.json)

        except ValidationError as e_:
            return f"{e_}", 400

        else:
            director = director_service.create(data)
            return f"Data added with id {director.id}", 201, {"location": f"directors/{director.id}"}


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):

    @directors_ns.doc(description='Get director by id')
    @directors_ns.response(200, "Success", director_model)
    @directors_ns.response(404, "Not found")
    def get(self, uid: int):
        director = director_service.get_one(uid)
        if not director:
            return f"director with id {uid} not found", 404

        return director_schema.dump(director), 200

    @directors_ns.doc(description='Update director', body=director_model)
    @directors_ns.response(200, "Success", director_model)
    @directors_ns.response(400, "Validation error")
    @directors_ns.response(404, "Not found")
    def put(self, uid: int):
        try:
            data = director_schema.load(request.json)
            director = director_service.get_one(uid)

            if not director:
                return f"director with id {uid} not found", 404
        except ValidationError as e_:
            return f"{e_}", 400

        else:
            director_service.update(uid, data)
            return f"Data updated with id {uid}", 200, {"location": f"directors/{director.id}"}

    @directors_ns.doc(description="Delete director by id")
    @directors_ns.response(204, "Success delete", director_model)
    @directors_ns.response(404, "director with this id not found")
    def delete(self, uid):
        director = director_service.get_one(uid)
        if not director:
            return f"director with id {uid} not found", 404

        return director_service.delete(director), 204
