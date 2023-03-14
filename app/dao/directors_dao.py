from typing import Type

from flask import request

from marshmallow import ValidationError
from sqlalchemy.orm import Session

from app.dao.models.directors import Director


class DirectorDao:

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_one(self, uid: int) -> Director:
        director = self.session.query(Director).get(uid)
        return director

    def get_all(self) -> list[Type[Director]]:
        directors = self.session.query(Director).all()
        return directors

    def post(self, data_load: dict) -> Director:
        director = Director(**data_load)
        self.session.add(director)
        self.session.commit()
        return director

    def put(self, uid: int, data: dict) -> None:
        self.session.query(Director).filter(Director.id == uid).update(data)
        self.session.commit()

    def delete(self, data: Director) -> None:
        self.session.delete(data)
        self.session.commit()
