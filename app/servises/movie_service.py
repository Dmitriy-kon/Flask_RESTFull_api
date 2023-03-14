from typing import Type

from app.dao.movies_dao import MoviesDao
from app.dao.models.movie import Movie


class MovieService:
    def __init__(self, dao: MoviesDao) -> None:
        self.dao = dao

    def get_one(self, mid: int) -> MoviesDao:
        return self.dao.get_one(mid)

    def get_all(self) -> list[Type[Movie]]:
        return self.dao.get_all()

    def create(self, data: dict) -> Movie:
        return self.dao.post(data)

    def update(self, uid: int, data: dict) -> None:
        return self.dao.put(uid, data)

    def partial_update(self, data: dict, uid: id) -> None:
        return self.dao.patch(data, uid)

    def delete(self, movie: Movie) -> None:
        return self.dao.delete(movie)

    @staticmethod
    def validate_data(data: dict):
        valid = set(data.keys()) <= {'title', 'description', 'year', 'trailer', 'rating', 'genre_id', 'director_id'}
        if valid:
            return data
        return None

    def filter(self, filters: dict) -> list[Type[Movie]]:
        return self.dao.filter(filters)
