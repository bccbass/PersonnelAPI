from datetime import datetime, timezone

from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(160), nullable=False)
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)
    albums = db.relationship('Album', back_populates='artist', cascade='all, delete')

    def __repr__(self):
        return f'<Artist "{self.name}">'

class ArtistSchema(ma.Schema):
    
    albums = fields.List(fields.Nested('AlbumSchema'), only=['title'])
    # Validators
    name = fields.String(required=True, validate=Length(min=1, max=80))
    date_created = fields.Date(load_default=datetime.now(timezone.utc))
    last_updated = fields.Date(load_default=datetime.now(timezone.utc))

    class Meta: 
        fields = ('id', 'name', 'albums')
        ordered = True

