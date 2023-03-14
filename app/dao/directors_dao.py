from flask import request

from marshmallow import ValidationError
from sqlalchemy.orm import Session

from app.dao.models import Director


class DirectorDao:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        directors = self.session. \
            query(Director.id,
                  Director.name).all()
        return directors_schema.dump(directors), 200

    def get_one(self, uid):
        director = self.session. \
            query(Director).get(uid)
        self.session.close()

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
            with self.session.begin():
                self.session.add(director)
            return '', 201

    def put(self, uid):
        try:
            load_data = director_schema.load(request.json)
            director = self.session.query(Director).get(uid)

            if not director:
                return f'Director with id {uid} not found', 404

        except ValidationError as _e:
            return f"{_e}", 400

        else:
            director.name = load_data.get("name")
            self.session.commit()
            self.session.close()
            return 'PUT completely', 201

    def delete(self, uid):
        director = self.session.query(Director).get(uid)

        if not director:
            return f'Director with id {uid} not found', 404

        self.session.delete(director)
        self.session.commit()
        self.session.close()
        return f"Director with id: {uid} successfully deleted", 201
