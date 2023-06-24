from init import db, ma
from marshmallow import fields, validates_schema

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)

    surname_groupname = db.Column(db.String(160), nullable=False)
    f_name = db.Column(db.String(160))
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)

    albums = db.relationship('Album', back_populates='artist')

    def __repr__(self):
        return f'<Track "{self.title}">'

class ArtistSchema(ma.Schema):
    albums = fields.List(fields.Nested('AlbumSchema'), only='title')

    class Meta: 
        fields = ('surname_groupname', 'f_name', 'albums')

