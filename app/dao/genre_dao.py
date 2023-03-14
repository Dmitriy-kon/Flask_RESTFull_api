from typing import Type

from sqlalchemy.orm import Session

from app.dao.models.genre import Genre


class GenreDao:

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_one(self, uid: int) -> Genre:
        genre = self.session.query(Genre).get(uid)
        return genre

    def get_all(self) -> list[Type[Genre]]:
        genres = self.session.query(Genre).all()
        return genres

    def post(self, data_load: dict) -> Genre:
        genre = Genre(**data_load)
        self.session.add(genre)
        self.session.commit()
        return genre

    def put(self, uid: int, data: dict) -> None:
        self.session.query(Genre).filter(Genre.id == uid).update(data)
        self.session.commit()

    def delete(self, data: Genre) -> None:
        self.session.delete(data)
        self.session.commit()

    # def update_partial(self, data: dict) -> None:
    #     pass
