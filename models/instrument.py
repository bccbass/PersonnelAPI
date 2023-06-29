from init import db, ma
from marshmallow import fields, validates_schema

class Instrument(db.Model):
    __tablename__ = 'instruments'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(160), nullable=False)
    date_created = db.Column(db.Date(), nullable=False)
    last_updated = db.Column(db.Date(), nullable=False)

    def __repr__(self):
        return f'<Instrument "{self.name}">'

    
class InstrumentSchema(ma.Schema):

    class Meta: 
        fields = ('id', 'name')
        ordered = True