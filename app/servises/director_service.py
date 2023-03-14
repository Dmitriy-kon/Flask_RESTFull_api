from typing import Type

from app.dao.directors_dao import DirectorDao
from app.dao.models.directors import Director


class DirectorService:
    def __init__(self, dao: DirectorDao) -> None:
        self.dao = dao

    def get_one(self, gid: int) -> DirectorDao:
        return self.dao.get_one(gid)

    def get_all(self) -> list[Type[Director]]:
        return self.dao.get_all()

    def create(self, data: dict) -> Director:
        return self.dao.post(data)

    def update(self, uid: int, data: dict) -> None:
        return self.dao.put(uid, data)

    def delete(self, director: Director) -> None:
        return self.dao.delete(director)
