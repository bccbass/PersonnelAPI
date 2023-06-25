from datetime import datetime, timezone

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db, ma
from models.track import Track, TrackSchema
from utilities import admin_verified

tracks_bp = Blueprint('tracks', __name__, url_prefix='/tracks')

# READ ONE TRACK:
@tracks_bp.route('/<int:track_id>')
@jwt_required()
def get_one_track(track_id):
    
    stmt = db.select(Track).filter_by(id=track_id)
    track = db.session.scalar(stmt)
    if track:
        return TrackSchema().dump(track)
    else:
        return {'erorr': 'Album not found'}, 404

# CREATE

@tracks_bp.route('/', methods=['POST'])
@jwt_required()
def create_track():
    admin_verified()
    try:
        track_req = TrackSchema().load(request.json)

        track = Track(
                # artist=track_req['artist'],
                title=track_req['title'],
                track_number=track_req.get('track_number', None),
                album_id=track_req.get('album_id', None),
                duration=track_req.get('duration', None),
                date_created=datetime.now(timezone.utc),
                last_updated=datetime.now(timezone.utc)
                )

        db.session.add(track)
        db.session.commit()
        return TrackSchema(exclude=['album']).dump(track), 201
    except:
        return {"error": "New tracks must have a valid title"}

@tracks_bp.route('/<int:track_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_track(track_id):
    admin_verified()

    stmt = db.select(Track).filter_by(id=track_id)
    track = db.session.scalar(stmt)
    if track:

        try:
            track_req = TrackSchema().load(request.json)

 
            # artist=track_req['artist'],
            track.title=track_req.get('title')
            track.album_id=track_req.get('album_id', track.album_id)
            track.track_number=track_req.get('track_number', track.track_number)
            track.duration=track_req.get('duration', track.duration)
            track.last_updated=datetime.now(timezone.utc)
                    

            db.session.add(track)
            db.session.commit()
            return TrackSchema(exclude=['album']).dump(track) 
        except:
            return {"error": ""}
        
    else:
        return {'erorr': 'Track not found'}, 404

# DELETE TRACK
@tracks_bp.route('/<int:track_id>', methods=['DELETE'])
@jwt_required()
def delete_track(track_id):
    admin_verified()
    stmt = db.select(Track).filter_by(id=track_id)
    track = db.session.scalar(stmt)
    if track:
        db.session.delete(track)
        db.session.commit()
        return {}, 200
    else:
        return {"error": "Track not found"}, 404

        



    