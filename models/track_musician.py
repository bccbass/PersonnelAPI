from init import db, ma 




class Track_Musician(db.Model):
    __name__ = 'track_musicians'
    # __bind_key__ = "track_musicians"

    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id', ondelete='CASCADE'), nullable=False)
    musician_id = db.Column(db.Integer, db.ForeignKey('musicians.id', ondelete='CASCADE'), nullable=False)
    date_created = db.Column(db.Date(), nullable=False)
    date_updated = db.Column(db.Date(), nullable=False)
    # created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
