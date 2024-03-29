from app.setup_bd import db

from marshmallow import fields, Schema


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
