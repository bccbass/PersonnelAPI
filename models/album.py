from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Length


class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='CASCADE'))
    release_date = db.Column(db.Date)
    img_url = db.Column(db.String)
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)
    
    
    artist = db.relationship('Artist', back_populates='albums')
    tracks = db.relationship('Track', back_populates='album') 

    def __repr__(self):
        return f'<ALBUM "{self.title}">'

class AlbumSchema(ma.Schema):
    # Validators
    title = fields.String(validate=Length(min=1, max=180))
    artist_id = fields.Integer()
    release_date = fields.Date()
    img_url = fields.Url()
    date_created = fields.Date()
    last_updated = fields.Date()

    # Nested Fields
    tracks = fields.List(fields.Nested('TrackSchema', only=['track_number', 'title']))
    artist = fields.Nested('ArtistSchema', only=['name', 'id'])
    
    class Meta:
        fields = ('id', 'title', 'artist', 'artist_id', 'release_date', 'img_url', 'tracks')
        ordered=True



