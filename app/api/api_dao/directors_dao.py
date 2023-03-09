from flask import request

from marshmallow import ValidationError

from app.models.model import db, Director, DirectorSchema

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()


class DirectorDao:
    def get_all(self):
        directors = db.session. \
            query(Director.id,
                  Director.name).all()
        return directors_schema.dump(directors), 200

    def get_one(self, uid):
        director = db.session. \
            query(Director).get(uid)
        db.session.close()

        if not director:
            return "Director, not found", 404

        return director_schema.dump(director), 200

    def post(self):
        try:
            load_data = request.json
            director = Director(**director_schema.load(load_data))

        except ValidationError as _e:
            return f'{_e}', 400

        else:
            with db.session.begin():
                db.session.add(director)
            return '', 201

    def put(self, uid):
        try:
            load_data = director_schema.load(request.json)
            director = db.session.query(Director).get(uid)

            if not director:
                return f'Director with id {uid} not found', 404

        except ValidationError as _e:
            return f"{_e}", 400

        else:
            director.name = load_data.get("name")
            db.session.commit()
            db.session.close()
            return 'PUT completely', 201

    def delete(self, uid):
        director = db.session.query(Director).get(uid)

        if not director:
            return f'Director with id {uid} not found', 404

        db.session.delete(director)
        db.session.commit()
        db.session.close()
        return f"Director with id: {uid} successfully deleted", 201
