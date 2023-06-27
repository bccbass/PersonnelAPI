from init import db, ma 
from marshmallow import fields

class Track_Musician(db.Model):
    __tablename__ = 'track_musician'
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer,  db.ForeignKey('tracks.id', ondelete='CASCADE'), nullable=False)
    musician_id = db.Column( db.Integer, db.ForeignKey('musicians.id', ondelete='CASCADE'), nullable=False)
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)

class Track_MusicianSchema(ma.Schema):
    track = fields.Nested('TrackSchema')
    musicians = fields.List(fields.Nested('MusicianSchema'))
    class Meta:
        fields = ('id', 'track_id', 'musician_id', 'track', 'musicians')