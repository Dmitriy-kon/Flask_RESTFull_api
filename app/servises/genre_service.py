from typing import Type

from app.dao.genre_dao import GenreDao
from app.dao.models.genre import Genre


class GenreService:
    def __init__(self, dao: GenreDao) -> None:
        self.dao = dao

    def get_one(self, gid: int) -> Genre:
        return self.dao.get_one(gid)

    def get_all(self) -> list[Type[Genre]]:
        return self.dao.get_all()

    def create(self, data: dict) -> Genre:
        return self.dao.post(data)

    def update(self, uid: int, data: dict) -> None:
        return self.dao.put(uid, data)

    def delete(self, genre: Genre) -> None:
        return self.dao.delete(genre)
