from datetime import datetime, timezone

from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required

from init import db, ma
from models.instrument import Instrument, InstrumentSchema
from utilities import admin_verified, locate_record, preexisting_record

instruments_bp = Blueprint('instruments', __name__, url_prefix='/instruments')

# GET ALL INSTRUMENTS:
@instruments_bp.route('/')
@jwt_required()
def get_instruments():
    # Returns a list of all available instrument records from the Database 
    # SQL: SELECT * FROM instruments;
    stmt = db.select(Instrument)
    instruments = db.session.scalars(stmt).all()
    return InstrumentSchema(many=True).dump(instruments)