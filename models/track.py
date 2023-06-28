from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Length





class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='CASCADE'))
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id', ondelete='CASCADE'))
    title = db.Column(db.String(255), nullable=False)
    track_number = db.Column(db.Integer)
    duration = db.Column(db.String(12))
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)
    musicians = db.relationship('Musician', secondary='track_musician', backref='tracks')
    album = db.relationship('Album', back_populates='tracks')
    artist = db.relationship('Artist')

    def __repr__(self):
        return f'<Track "{self.title}">'
    
class TrackSchema(ma.Schema):
    # Validators
    artist_id = fields.Integer()
    album_id = fields.Integer()
    track_number = fields.Integer()
    # duration = fields.Time()
    


    musicians = fields.List(fields.Nested('MusicianSchema'), exclude=['tracks'])
    album = fields.Nested('AlbumSchema', only=['id', 'title'])
    artist = fields.Nested('ArtistSchema', only=['id', 'name'])
    class Meta:
        fields = ('id', 'title', 'artist', 'artist_id', 'album', 'album_id' 'duration', 'track_number', 'musicians' )
        ordered=True