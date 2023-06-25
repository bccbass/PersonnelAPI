from flask import Blueprint
from marshmallow import fields, validates_schema
from flask_jwt_extended import jwt_required

from init import db, ma 
from models.album import Album, AlbumSchema
from models.track import Track, TrackSchema
from utilities import admin_verified   

global_bp = Blueprint('global', __name__, url_prefix='global')


# THIS SHOULD BE AN EXTENDED ROUTE AS IT HAS MULTIFUNCTIONAL THINGS HAPPENING

@global_bp.route('/', methods=['POST'])
@jwt_required()
def create_track():
    admin_verified()
    track_req = TrackSchema().load(request.json)

    album=Album(
        title=track_req['album']['title'],
        artist=track_req['album']['artist'],
        label=track_req['album']['label'],
        release_date=track_req['album']['release_date'],
        genre=track_req['album']['genre'],
        img_url=track_req['album']['img_url'],
        date_created= datetime.now(timezone.utc),
        last_updated= datetime.now(timezone.utc)
        )
    
    db.session.add(album)
    db.session.commit()

    track = Track(
            # artist=track_req['artist'],
            title=track_req['title'],
            album_id=album.id,
            track_number=track_req.get('track_number', None),
            duration=track_req.get('duration', None),
            date_created=datetime.now(timezone.utc),
            last_updated=datetime.now(timezone.utc),
            )

    db.session.add(track)
    db.session.commit()
    return TrackSchema().dump(track) 
