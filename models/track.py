from init import db, ma 
from models.track_musician import track_musician




class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id', ondelete='CASCADE'))
    title = db.Column(db.String(255), nullable=False)
    track_number = db.Column(db.Integer, unique=True)
    duration = db.Column(db.String(12))
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)
    # created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    musicians = db.relationship('Musician', secondary=track_musician, backref='tracks')

    def __repr__(self):
        return f'<Track "{self.title}">'