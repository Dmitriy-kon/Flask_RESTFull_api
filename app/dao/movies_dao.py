from flask import request
from sqlalchemy.orm import Query, Session

from app.dao.models.movie import MovieSchema, Movie
from app.dao.models.directors import Director
from app.dao.models.genre import Genre

# CRUD
class MoviesDao:

    def __init__(self, session: Session):
        self.session = session

    def __get_query(self) -> Query:
        movies_query = self.session. \
            query(Movie.id,
                  Movie.title,
                  Movie.description,
                  Movie.year,
                  Movie.trailer,
                  Movie.rating,
                  Genre.name.label("genre"),
                  Director.name.label("director")
                  ).join(Movie.genre).join(Movie.director)
        self.session.close()
        return movies_query

    def get_all(self):
        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)

        if director_id and genre_id:
            movies = self.__get_query() \
                .filter(Movie.director_id == director_id, Movie.genre_id == genre_id).all()

            return movies

            # TODO: перенести логику из фильмов дао в сервисы фильмы
            # if not movies:
            #     return "id not found", 404
            # return movies_schema.dump(movies), 200

        # elif director_id:
        #     movies = self.__get_query() \
        #         .filter(Movie.director_id == director_id).all()
        #     if not movies:
        #         return "id not found", 404
        #     return movies_schema.dump(movies), 200
        #
        # elif director_id:
        #     movies = self.__get_query() \
        #         .filter(Movie.genre_id == genre_id).all()
        #     if not movies:
        #         return "id not found", 404
        #     return movies_schema.dump(movies), 200

        else:
            movies = self.__get_query().all()
            return movies
            # return movies_schema.dump(movies), 200

    def get_one(self, uid: int):
        movie = self.__get_query().filter(Movie.id == uid).one()
        return movie
        # if not movie:
        #     return "id not found", 404
        # return movie_schema.dump(movie), 200
