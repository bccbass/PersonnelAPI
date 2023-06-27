from init import db, ma 
from marshmallow import fields, validates_schema




class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='CASCADE'))
    label = db.Column(db.String(100))
    release_date = db.Column(db.Date)
    img_url = db.Column(db.String)
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)
    
    
    artist = db.relationship('Artist', back_populates='albums')
    tracks = db.relationship('Track', back_populates='album') 

    def __repr__(self):
        return f'<ALBUM "{self.title}">'

class AlbumSchema(ma.Schema):
    tracks = fields.List(fields.Nested('TrackSchema', only=['title', 'musicians']))
    artist = fields.Nested('ArtistSchema', only=['name', 'id'])
    class Meta:
        fields = ('id', 'title', 'artist', 'release_date', 'img_url', 'tracks', 'label')
        ordered=True



