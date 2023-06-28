from datetime import datetime, timezone

from init import db, ma 
from marshmallow import fields
from marshmallow.validate import Length 




class Musician(db.Model):
    __tablename__ = 'musicians'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(255), nullable=False)
    l_name = db.Column(db.String(255), nullable=False)
    instrument_id = db.Column(db.Integer, db.ForeignKey('instruments.id'), nullable=False)
    birthdate = db.Column(db.Date)
    expiry = db.Column(db.Date)
    img_url = db.Column(db.String)
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)
    # created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # tracks = db.relationship('Track', secondary=track_musician, backref='musicians')
    instrument = db.relationship('Instrument')
    def __repr__(self):
        return f'<Musician "{self.f_name} {self.l_name}: {self.instrument}">'
    
class MusicianSchema(ma.Schema):
    # Validators:
    f_name = fields.String(validate=Length(min=1, max=80))
    l_name = fields.String(validate=Length(min=1, max=80))
    instrument_id= fields.Int()
    birthdate = fields.Date()
    expiry = fields.Date()
    img_url = fields.String()
    date_created = fields.Date()
    last_updated = fields.Date()

    instrument = fields.Nested('InstrumentSchema', only=['name'])
    class Meta:
        fields = ('id', 'f_name', 'l_name', 'instrument', 'birthdate', 'expiry', 'img_url', 'instrument_id')
        ordered = True