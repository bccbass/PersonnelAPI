from marshmallow import fields
from marshmallow.validate import Length, And, Regexp


from init import db, ma

char_value = '^[a-zA-Z0-9 ]+$'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, nullable=False)
    last_updated = db.Column(db.Date, nullable=False)

class UserSchema(ma.Schema):
    # Validators:
    name = fields.String(validate=And(
        Length(min=1, max=80),
        Regexp(char_value, error='Letters, numbers and spaces only are allowed')))
    email = fields.Email()
    password = fields.String(validate=Length(min=8, max=20))
    is_admin = fields.Boolean()
    date_created = fields.Date()
    last_updated = fields.Date()

    class Meta:
        fields = ('name', 'email', 'id', 'password', 'is_admin', 'date_created', 'last_updated')