from core.models.model import db, Movie, Genre, Director, MovieSchema, GenreSchema, DirectorSchema

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()

class MoviesDao:
    def get_all(self):
        movies = db.session.query(Movie).limit(10).all()
        return movies_schema.dump(movies)

    def get_one(self, id):
        movie = db.session.query(Movie).get(id)
        return movie_schema.dump(movie)
