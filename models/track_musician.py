from init import db, ma 

class Track_Musician(db.Model):
    __tablename__ = 'track_musician'
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer,  db.ForeignKey('tracks.id', ondelete='CASCADE'), nullable=False)
    musician_id = db.Column( db.Integer, db.ForeignKey('musicians.id', ondelete='CASCADE'), nullable=False)
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)