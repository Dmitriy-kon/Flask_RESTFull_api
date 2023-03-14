from typing import Type

from sqlalchemy.orm import Session

from app.dao.models.movie import Movie


# CRUD
class MoviesDao:

    def __init__(self, session: Session):
        self.session = session

    def get_one(self, uid: int) -> Movie:
        movie = self.session.query(Movie).get(uid)
        return movie

    def get_all(self) -> list[Type[Movie]]:
        movies = self.session.query(Movie).all()
        return movies

    def post(self, data_load: dict) -> Movie:
        movie = Movie(**data_load)
        self.session.add(movie)
        self.session.commit()
        return movie

    def put(self, uid: int, data: dict) -> None:
        self.session.query(Movie).filter(Movie.id == uid).update(data)
        self.session.commit()

    def delete(self, data: Movie) -> None:
        self.session.delete(data)
        self.session.commit()

    def patch(self, data: dict, uid: int) -> None:
        self.session.query(Movie).filter(Movie.id == uid).update(data)
        self.session.commit()

    def filter(self, filters: dict[str, int | str]) -> list[Type[Movie]]:
        movies = self.session.query(Movie)

        if filters['director_id']:
            movies = movies.filter(Movie.director_id == filters['director_id'])
        if filters['genre_id']:
            movies = movies.filter(Movie.genre_id == filters['genre_id'])
        if filters['year']:
            movies = movies.filter(Movie.year == filters['year'])

        return movies.all()
