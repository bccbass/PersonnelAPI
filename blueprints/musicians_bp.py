from datetime import datetime, timezone

from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required

from init import db, ma
from models.musician import Musician, MusicianSchema
from utilities import admin_verified, locate_record, preexisting_record

musicians_bp = Blueprint('musicians', __name__, url_prefix='/musicians')


# READ ALL MUSICIANS:
@musicians_bp.route('/')
def get_musicians():
    # Returns all available Musician records from the Database 
    # SQL: SELECT * FROM musicians;
    stmt = db.select(Musician)
    musicians = db.session.scalars(stmt)
    return MusicianSchema(many=True, only=['f_name', 'l_name', 'instrument']).dump(musicians)

# READ ONE MUSICIAN:
@musicians_bp.route('/<int:musician_id>')
@jwt_required()
def get_one_musician(musician_id):
    # Returns one musician record, filtered by musician ID recieved from <musician_id>
    # SQL: SELECT * FROM musicians WHERE id=<musician_id>;
    musician = locate_record(Musician, musician_id)
    return MusicianSchema(exclude=['instrument_id']).dump(musician)

# CREATE A NEW MUSICIAN:
@musicians_bp.route('/', methods=['POST'])
@jwt_required()
def create_musician():
    admin_verified()
    musician_req = MusicianSchema().load(request.json)

    # check if musician already exists:
    # Searches for one musician, filtered by musicians first and last name obtained from JSON request
    # SQL: SELECT * FROM musicians WHERE f_name=musician_req['f_name'] AND l_name=musician_req['l_name'];
    stmt = db.select(Musician).filter_by(f_name=musician_req['f_name'], l_name=musician_req['l_name'])
    preexisting_record(stmt)    

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
    
    # Returns one musician record, filtered by musician ID recieved from <musician_id>
    # SQL: SELECT * FROM musicians WHERE id=<musician_id>;
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

    # Returns one musician record, filtered by musician ID recieved from <musician_id>
    # SQL: SELECT * FROM musicians WHERE id=<musician_id>;
    musician = locate_record(Musician, musician_id)

    db.session.delete(musician)
    db.session.commit()
    return {'Message': f'Musician <{musician.f_name} {musician.l_name}> with id <{musician_id}> successfully deleted'}, 200

        