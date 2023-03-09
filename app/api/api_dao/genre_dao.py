from flask import request

from marshmallow import ValidationError

from app.models.model import db, Genre, GenreSchema

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


class GenreDao:

    def get_all(self):
        genres = db.session.query(Genre).all()
        return genres_schema.dump(genres), 200

    def post(self):
        try:
            data_load = genre_schema.load(request.json)
            genre = Genre(**data_load)
        except ValidationError as _e:
            return f"{_e}", 404
        else:
            with db.session.begin():
                db.session.add(genre)
            return 'Genre added', 201

    def get_one(self, uid):
        genre = db.session.query(Genre).get(uid)
        db.session.close()

        if not genre:
            return "genre not found", 404

        return genre_schema.dump(genre), 200

    def put(self, uid):
        try:
            data_load = genre_schema.load(request.json)
            genre = db.session.query(Genre).get(uid)

            if not genre:
                return "genre not found", 404

        except ValidationError as _e:
            return f"{_e}", 400

        else:
            genre.name = data_load.get("name")
            db.session.commit()
            db.session.close()
            return "PUT completely", 201

    def delete(self, uid):
        genre = db.session.query(Genre).get(uid)

        if not genre:
            return "genre not found", 404

        db.session.delete(genre)
        db.session.commit()
        db.session.close()

        return f"Genre with id: {uid} successfully deleted", 201
