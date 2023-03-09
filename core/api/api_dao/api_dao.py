from flask import request

from core.models.model import db, Movie, Genre, Director, MovieSchema, GenreSchema, DirectorSchema

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


class MoviesDao:
    def get_all(self):
        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)
        if director_id and genre_id:
            movies = db.session. \
                query(Movie.id,
                      Movie.title,
                      Movie.description,
                      Movie.year,
                      Movie.trailer,
                      Movie.rating,
                      Genre.name.label("genre"),
                      Director.name.label("director")
                      ).join(Movie.genre).join(Movie.director) \
                .filter(Movie.director_id == director_id, Movie.genre_id == genre_id).all()
            return movies_schema.dump(movies)

        elif director_id:
            movies = db.session. \
                query(Movie.id,
                      Movie.title,
                      Movie.description,
                      Movie.year,
                      Movie.trailer,
                      Movie.rating,
                      Genre.name.label("genre"),
                      Director.name.label("director")
                      ).join(Movie.genre).join(Movie.director) \
                .filter(Movie.director_id == director_id).all()
            return movies_schema.dump(movies)

        elif director_id:
            movies = db.session. \
                query(Movie.id,
                      Movie.title,
                      Movie.description,
                      Movie.year,
                      Movie.trailer,
                      Movie.rating,
                      Genre.name.label("genre"),
                      Director.name.label("director")
                      ).join(Movie.genre).join(Movie.director) \
                .filter(Movie.genre_id == genre_id).all()
            return movies_schema.dump(movies)

        else:
            movies = db.session. \
                query(Movie.id,
                      Movie.title,
                      Movie.description,
                      Movie.year,
                      Movie.trailer,
                      Movie.rating,
                      Genre.name.label("genre"),
                      Director.name.label("director")
                      ).join(Movie.genre).join(Movie.director).all()
            return movies_schema.dump(movies)

    def get_one(self, id):
        movie = db.session. \
            query(Movie.id,
                  Movie.title,
                  Movie.description,
                  Movie.year,
                  Movie.trailer,
                  Movie.rating,
                  Genre.name.label("genre"),
                  Director.name.label("director")
                  ).join(Movie.genre).join(Movie.director).filter(Movie.id == id).one()
        return movie_schema.dump(movie)
