from app.setup_bd import db

from marshmallow import fields, Schema


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
