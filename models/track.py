from init import db, ma 
from marshmallow import fields, validates_schema





class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='CASCADE'))
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id', ondelete='CASCADE'))
    title = db.Column(db.String(255), nullable=False)
    track_number = db.Column(db.Integer, unique=True)
    duration = db.Column(db.String(12))
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)
    musicians = db.relationship('Musician', secondary='track_musician', backref='tracks')
    album = db.relationship('Album', back_populates='tracks')
    artist = db.relationship('Artist')

    def __repr__(self):
        return f'<Track "{self.title}">'
    
class TrackSchema(ma.Schema):
    musicians = fields.List(fields.Nested('MusicianSchema'), exclude=['birthdate', 'expiry', 'date_created', 'last_updated'])
    album = fields.Nested('AlbumSchema', only=['id', 'title'])
    artist = fields.Nested('ArtistSchema', only=['id', 'name'])
    class Meta:
        fields = ('id', 'title', 'artist', 'track_number', 'duration', 'musicians', 'album_id', 'album')