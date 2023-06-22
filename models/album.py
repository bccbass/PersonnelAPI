from init import db, ma 
from marshmallow import fields, validates_schema




class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    # artist_given_name = db.Column(db.String(100))
    label = db.Column(db.String(100))
    release_date = db.Column(db.Date)
    genre = db.Column(db.String(100))
    img_url = db.Column(db.String)
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)
    
    
    # created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tracks = db.relationship('Track', back_populates='album') 

    def __repr__(self):
        return f'<ALBUM "{self.artist}: {self.title}">'

class AlbumSchema(ma.Schema):
    tracks = fields.List(fields.Nested('Track', exclude=['album_id', 'date_created', 'last_updated']))
    class Meta:
        fields = ('id', 'title', 'artist', 'release_date', 'genre', 'img_url')




