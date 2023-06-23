from sqlalchemy import TIMESTAMP
from marshmallow import fields

from init import db, ma


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # create user role:
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, nullable=False)
    last_updated = db.Column(db.Date, nullable=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email', 'id', 'password', 'is_admin', 'date_created', 'last_updated')