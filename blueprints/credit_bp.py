from datetime import datetime, timezone

from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required

from init import db
from models.track_musician import Track_Musician, Track_MusicianSchema
from utilities import admin_verified, locate_record, locate_stmt, preexisting_record

credit_bp = Blueprint('credit', __name__,  url_prefix='/credit')

# CREATE CREDIT (TRACK_MUSICIAN ASSOCIATION)
@credit_bp.route('/', methods=['POST'])
def create_credit():
    credit_req = Track_MusicianSchema().load(request.json)
    stmt = db.select(Track_Musician).filter_by(musician_id=credit_req['musician_id'], track_id=credit_req['track_id'])
    preexisting_record(stmt)

    credit = Track_Musician(
        track_id = credit_req['track_id'],
        musician_id = credit_req['musician_id'],
        date_created= datetime.now(timezone.utc),
        last_updated= datetime.now(timezone.utc)

    )

    db.session.add(credit)
    db.session.commit()

    return Track_MusicianSchema().dump(credit), 201



# DELETE CREDIT (TRACK_MUSICIAN ASSOCIATION)
@credit_bp.route('/<int:credit_id>', methods=['DELETE'])
def delete_credit(credit_id):
    if credit_id > 0:
        # Returns one track_record record from the Database filtered by id, obtained from <credit_id>
        # SQL: SELECT * FROM track_musician where id=<credit_id>;
        credit = locate_record(Track_Musician, credit_id)
        db.session.delete(credit)
        db.session.commit()

    if credit_id == 0:
        # Returns one track_record record from the Database filtered by track id and musician id, obtained from user query string
        # SQL: SELECT * FROM track_musician where musician_id=request.args['musician_id'] AND track_id=request.args['track_id'];
        stmt = db.select(Track_Musician).filter_by(musician_id=request.args['musician_id'], track_id=request.args['track_id'])
        credit = locate_stmt(stmt)

    db.session.delete(credit)
    db.session.commit()
    return {'Message': "Successfully deleted track credit"}, 200