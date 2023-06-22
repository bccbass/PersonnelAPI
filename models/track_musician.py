from init import db, ma 





# track_musician = db.Table('track_musician',
#     # id = db.Column(db.Integer, primary_key=True)
#     db.Column('track_id', db.Integer, db.ForeignKey('tracks.id', ondelete='CASCADE'), nullable=False),
#     db.Column('musician_id', db.Integer, db.ForeignKey('musicians.id', ondelete='CASCADE'), nullable=False)
#     # db.Column('date_created', db.Date(), nullable=False),
#     # db.Column('date_updated', db.Date(), nullable=False)
#     # created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

#     # track = db.relationship('Track', back_populates='track_musicians')
#     # musician = db.relationship('Musician', back_populates='track_musicians')
# )

class Track_Musician(db.Model):
    __tablename__ = 'track_musician'
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer,  db.ForeignKey('tracks.id', ondelete='CASCADE'), nullable=False)
    musician_id = db.Column( db.Integer, db.ForeignKey('musicians.id', ondelete='CASCADE'), nullable=False)
    date_created = db.Column(db.Date(), nullable=False)
    date_updated = db.Column(db.Date(), nullable=False)