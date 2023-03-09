from flask import request
from sqlalchemy.orm import Query

from app.models.model import db, Movie, Genre, Director, MovieSchema

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


class MoviesDao:

    @staticmethod
    def __get_query() -> Query:
        movies_querry = db.session. \
            query(Movie.id,
                  Movie.title,
                  Movie.description,
                  Movie.year,
                  Movie.trailer,
                  Movie.rating,
                  Genre.name.label("genre"),
                  Director.name.label("director")
                  ).join(Movie.genre).join(Movie.director)
        db.session.close()
        return movies_querry

    def get_all(self):
        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)

        if director_id and genre_id:
            movies = self.__get_query() \
                .filter(Movie.director_id == director_id, Movie.genre_id == genre_id).all()
            if not movies:
                return "id not found", 404
            return movies_schema.dump(movies), 200

        elif director_id:
            movies = self.__get_query() \
                .filter(Movie.director_id == director_id).all()
            if not movies:
                return "id not found", 404
            return movies_schema.dump(movies), 200

        elif director_id:
            movies = self.__get_query() \
                .filter(Movie.genre_id == genre_id).all()
            if not movies:
                return "id not found", 404
            return movies_schema.dump(movies), 200

        else:
            movies = self.__get_query().all()
            return movies_schema.dump(movies), 200

    def get_one(self, uid: int):
        movie = self.__get_query().filter(Movie.id == uid).one()
        if not movie:
            return "id not found", 404
        return movie_schema.dump(movie), 200
