from datetime import datetime, timezone

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db, ma
from models.musician import Musician, MusicianSchema
from utilities import admin_verified, locate_record

musicians_bp = Blueprint('musicians', __name__, url_prefix='/musicians')


# READ ALL MUSICIANS:
@musicians_bp.route('/')
def get_musicians():
    stmt = db.select(Musician)
    musicians = db.session.scalars(stmt)
    return MusicianSchema(many=True, only=['f_name', 'l_name', 'instrument']).dump(musicians)

# READ ONE MUSICIAN:
@musicians_bp.route('/<int:musician_id>')
@jwt_required()
def get_one_musician(musician_id):
    musician = locate_record(Musician, musician_id)
    return MusicianSchema(exclude=['instrument_id']).dump(musician)

# CREATE A NEW MUSICIAN:
@musicians_bp.route('/', methods=['POST'])
@jwt_required()
def create_musician():
    admin_verified()
    musician_req = MusicianSchema().load(request.json)

    # check if musician already exists:
    stmt = db.select(Musician).filter_by(f_name=musician_req['f_name'], l_name=musician_req['l_name'])
    existing_musician = db.session.scalar(stmt)
    if existing_musician:
        return {'error': 'Musician already exists'}
    
    else: 
            musician = Musician(
            f_name = musician_req['f_name'],
            l_name = musician_req['l_name'],
            instrument_id = musician_req.get('instrument_id', 8),
            birthdate = musician_req.get('birthdate', None),
            expiry = musician_req.get('expiry', None),
            img_url = musician_req.get('img_url', None),
            date_created=datetime.now(timezone.utc),
            last_updated=datetime.now(timezone.utc)
            )

            db.session.add(musician)
            db.session.commit()

            return MusicianSchema().dump(musician), 201

# UPDATE MUSICIAN:
@musicians_bp.route('/<int:musician_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_musician(musician_id):
    admin_verified()
    musician_req = MusicianSchema().load(request.json)

    musician = locate_record(Musician, musician_id)

    musician.f_name = musician_req.get('f_name', musician.f_name)
    musician.l_name = musician_req.get('l_name', musician.l_name)
    musician.instrument_id = musician_req.get('instrument_id', musician.instrument_id)
    musician.birthdate = musician_req.get('birthdate', musician.birthdate)
    musician.expiry = musician_req.get('expiry', musician.expiry)
    musician.img_url = musician_req.get('img_url', musician.img_url)
    musician.last_updated=datetime.now(timezone.utc)
         
    db.session.add(musician)
    db.session.commit()

    return MusicianSchema().dump(musician), 201


# DELETE MUSICIAN:
@musicians_bp.route('/<int:musician_id>', methods=['DELETE'])
@jwt_required()
def delete_musician(musician_id):
    admin_verified()
    musician = locate_record(Musician, musician_id)

    db.session.delete(musician)
    db.session.commit()
    return {}, 200

        