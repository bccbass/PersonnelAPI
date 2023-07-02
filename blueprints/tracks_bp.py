from datetime import datetime, timezone

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db, ma
from models.track import Track, TrackSchema
from utilities import admin_verified, locate_record, preexisting_record

tracks_bp = Blueprint('tracks', __name__, url_prefix='/tracks')

# READ ONE TRACK:
@tracks_bp.route('/<int:track_id>')
@jwt_required()
def get_one_track(track_id):
    track = locate_record(Track, track_id)
    return TrackSchema(exclude=['musicians.tracks', 'musicians.birthdate', 'musicians.expiry', 'musicians.instrument_id', 'artist_id', 'album_id']).dump(track)

# CREATE TRACK:
@tracks_bp.route('/', methods=['POST'])
@jwt_required()
def create_track():
    admin_verified()
    track_req = TrackSchema().load(request.json)

    track = Track(
            artist_id=track_req['artist_id'],
            title=track_req['title'],
            track_number=track_req.get('track_number', None),
            album_id=track_req.get('album_id', None),
            duration=track_req.get('duration', None),
            date_created=datetime.now(timezone.utc),
            last_updated=datetime.now(timezone.utc)
            )

    db.session.add(track)
    db.session.commit()
    return TrackSchema(exclude=['artist_id']).dump(track), 201

# UPDATE TRACK 
@tracks_bp.route('/<int:track_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_track(track_id):
    admin_verified()
    track = locate_record(Track, track_id)
    
    track_req = TrackSchema().load(request.json)
    
    track.artist_id=track_req.get('artist_id', track.artist_id),
    track.title=track_req.get('title', track.title)
    track.album_id=track_req.get('album_id', track.album_id)
    track.track_number=track_req.get('track_number', track.track_number)
    track.duration=track_req.get('duration', track.duration)
    track.last_updated=datetime.now(timezone.utc)
                    

    db.session.add(track)
    db.session.commit()
    return TrackSchema(exclude=['artist_id', 'album_id', 'musicians.tracks']).dump(track) 


# DELETE TRACK
@tracks_bp.route('/<int:track_id>', methods=['DELETE'])
@jwt_required()
def delete_track(track_id):
    admin_verified()
    track = locate_record(Track, track_id)
    db.session.delete(track)
    db.session.commit()
    return {'Message': f'Track with title <{track.title}> and id <{track_id}> succesfully deleted!'}, 200


        



    