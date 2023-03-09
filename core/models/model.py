from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema

db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    year = db.Column(db.Integer)
    trailer = db.Column(db.String(100))
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))

    genre = db.relationship("Genre")
    director = db.relationship("Director", back_populates='movies')


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    movies = db.relationship("Movie")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    year = fields.Int()
    trailer = fields.Str()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Str()
    director = fields.Str()


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
