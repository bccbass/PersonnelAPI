from init import db, ma 
# from models.track_musician import track_musician





class Musician(db.Model):
    __tablename__ = 'musicians'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(255), nullable=False)
    l_name = db.Column(db.String(255), nullable=False)
    instrument = db.Column(db.String(120), nullable=False)
    birthdate = db.Column(db.Date)
    expiry = db.Column(db.Date)
    img_url = db.Column(db.String)
    date_created = db.Column(db.Date(), nullable=False)
    date_updated = db.Column(db.Date(), nullable=False)
    # created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # tracks = db.relationship('Track', secondary=track_musician, backref='musicians')
    def __repr__(self):
        return f'<Musician "{self.f_name} {self.l_name}: {self.instrument}">'