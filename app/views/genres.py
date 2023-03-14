from app.container import genre_service
from app.dao.models.genre import GenreSchema

from flask_restx import Namespace, Resource, fields
from marshmallow import ValidationError
from flask import request

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

# Genre model for documentation
genre_model = genres_ns.model("Genre", {
    "id": fields.Integer(required=False, description="Genre identification"),
    "name": fields.String(required=True, description="Genre name")
})


@genres_ns.route('/')
class GenresView(Resource):
    @genres_ns.doc(description="Get genres",
                   params={
                       "id": "genre id",
                       "name": "genre name"
                   })
    @genres_ns.response(200, "Success", genre_model)
    @genres_ns.response(404, "Not found")
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    @genres_ns.doc(description="add new genre", body=genre_model)
    @genres_ns.response(201, "Created")
    @genres_ns.response(400, "Validation Error")
    def post(self):
        try:
            data = genre_schema.load(request.json)

        except ValidationError as e_:
            return f"{e_}", 400

        else:
            genre = genre_service.create(data)
            return f"Data added with id {genre.id}", 201, {"location": f"genres/{genre.id}"}


@genres_ns.route('/<int:uid>')
class GenreView(Resource):
    @genres_ns.doc(description='Get genre by id')
    @genres_ns.response(200, "Success", genre_model)
    @genres_ns.response(404, "Not found")
    def get(self, uid):
        genre = genre_service.get_one(uid)
        if not genre:
            return f"genre with id {uid} not found", 404

        return genre_schema.dump(genre), 200

    @genres_ns.doc(description='Update genre', body=genre_model)
    @genres_ns.response(200, "Success", genre_model)
    @genres_ns.response(400, "Validation error")
    @genres_ns.response(404, "Not found")
    def put(self, uid):
        try:
            data = genre_schema.load(request.json)
            genre = genre_service.get_one(uid)

            if not genre:
                return f"genre with id {uid} not found", 404

        except ValidationError as e_:
            return f"{e_}", 400

        else:
            genre_service.update(uid, data)
            return f"Data updated with id {uid}", 200, {"location": f"genres/{genre.id}"}

    @genres_ns.doc(description='Delete genre by id')
    @genres_ns.response(204, "Success delete", genre_model)
    @genres_ns.response(404, "genre with this id not found")
    def delete(self, uid):
        genre = genre_service.get_one(uid)
        if not genre:
            return f"genre with id {uid} not found", 404

        return genre_service.delete(genre), 204

    # @genres_ns.doc(description='patch genre by id', body=genre_model)
    # @genres_ns.response(200, "Success")
    # @genres_ns.response(400, "Validation error")
    # @genres_ns.response(404, "Not found")
    # def patch(self, uid):
    #     try:
    #         data = genre_schema.load(request.json)
    #         genre = genre_service.get_one(uid)
    #
    #         if not genre:
    #             return f"genre with id {uid} not found", 404
    #
    #     except ValidationError as e_:
    #         return f"{e_}", 400
    #     else:
    #         return genre_service.update_partial(data), 200
