from app.container import movie_service
from app.dao.models.movie import MovieSchema

from flask_restx import Namespace, Resource, fields
from marshmallow import ValidationError
from flask import request

movies_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

# Movie model for documentation
movie_model = movies_ns.model("Movie", {
    "id": fields.Integer(required=False, description="Movie identification"),
    "title": fields.String(required=True, description="title name"),
    "description": fields.String(required=True, description="movie description"),
    "year": fields.Integer(required=True, description="movie year"),
    "trailer": fields.String(required=True, description="trailer url"),
    "rating": fields.Float(required=True, description="movie rating"),
    "genre_id": fields.Integer(required=True, description="genre id"),
    "director_id": fields.Integer(required=True, description="director id")

})


@movies_ns.route('/')
class MoviesView(Resource):

    @movies_ns.doc(description="Get movies")
    @movies_ns.response(200, "Success", movie_model)
    @movies_ns.response(404, "Not found")
    def get(self):
        filters = {
            'director_id': request.args.get('director_id', type=int),
            'genre_id': request.args.get('genre_id', type=int),
            'year': request.args.get('year', type=int)
        }

        movies_found = movie_service.filter(filters)

        if not movies_found:
            return f"movie with your filters not found", 404

        return movies_schema.dump(movies_found), 200

    @movies_ns.doc(description="add new movie", body=movie_model)
    @movies_ns.response(201, "Created")
    @movies_ns.response(400, "Validation Error")
    def post(self):
        try:
            data = movie_schema.load(request.json)
        except ValidationError as e_:
            return f"{e_}", 400

        else:
            movie = movie_service.create(data)
            return f"Data added with id {movie.id}", 201, {"location": f"movies/{movie.id}"}


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    @movies_ns.doc(description='Get movie by id')
    @movies_ns.response(200, "Success", movie_model)
    @movies_ns.response(404, "Not found")
    def get(self, uid):
        movie = movie_service.get_one(uid)
        if not movie:
            return f"movie with id {uid} not found", 404

        return movie_schema.dump(movie), 200

    @movies_ns.doc(description='Update movie', body=movie_model)
    @movies_ns.response(200, "Success", movie_model)
    @movies_ns.response(400, "Validation error")
    @movies_ns.response(404, "Not found")
    def put(self, uid: int):
        try:
            data = movie_schema.load(request.json)
            movie = movie_service.get_one(uid)

            if not movie:
                return f"movie with id {uid} not found", 404
        except ValidationError as e_:
            return f"{e_}", 400

        else:
            movie_service.update(uid, data)
            return f"Data updated with id {uid}", 200, {"location": f"movies/{movie.id}"}

    @movies_ns.doc(description="Delete movie by id")
    @movies_ns.response(204, "Success delete", movie_model)
    @movies_ns.response(404, "movie with this id not found")
    def delete(self, uid):
        movie = movie_service.get_one(uid)
        if not movie:
            return f"movie with id {uid} not found", 404

        return movie_service.delete(movie), 204

    @movies_ns.doc(description='Partial update movie', body=movie_model)
    @movies_ns.response(200, "Success", movie_model)
    @movies_ns.response(400, "Validation error")
    @movies_ns.response(404, "Not found")
    def patch(self, uid: int):
        movie = movie_service.get_one(uid)
        data = movie_service.validate_data(request.json)

        if not data:
            return "Validation error", 400

        if not movie:
            return f"movie with id {uid} not found", 404

        return movie_service.partial_update(data, uid), 200
