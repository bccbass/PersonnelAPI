from datetime import datetime, timezone

from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required

from init import db, ma
from models.artist import Artist, ArtistSchema
from utilities import admin_verified, locate_record

artists_bp = Blueprint('artists', __name__, url_prefix='/artists')

# READ ALL ARTISTS:
@artists_bp.route('/')
def get_artists():
    stmt = db.select(Artist)
    artists = db.session.scalars(stmt)
    return ArtistSchema(many=True, exclude=['albums.artist', 'albums.tracks']).dump(artists)

# READ ONE ARTIST:
@artists_bp.route('/<int:artist_id>')
@jwt_required()
def get_one_artist(artist_id):
    artist = locate_record(Artist, artist_id)
    return ArtistSchema().dump(artist)


# CREATE ARTIST
@artists_bp.route('/', methods=['POST'])
@jwt_required()
def create_artist():
    admin_verified()

    artist_req = ArtistSchema().load(request.json)

    # Check Artist doesn't already exist:
    stmt = db.select(Artist).filter_by(name=artist_req['name'])
    existing_artist = db.session.scalar(stmt)
    if existing_artist:
        abort(400, description="Artist already exists")

    artist = Artist(
            name=artist_req['name'],
            albums=artist_req.get('albums', []),
            date_created=datetime.now(timezone.utc),
            last_updated=datetime.now(timezone.utc)
            )

    db.session.add(artist)
    db.session.commit()
    return ArtistSchema().dump(artist), 201


# UPDATE ARTIST
@artists_bp.route('/<int:artist_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_artist(artist_id):
    admin_verified()
    artist = locate_record(Artist, artist_id)

    artist_req = ArtistSchema().load(request.json)

    artist.name=artist_req.get('name', artist.name)
    artist.last_updated=datetime.now(timezone.utc)
                    
    db.session.add(artist)
    db.session.commit()
    return ArtistSchema(exclude=['albums']).dump(artist) 


# DELETE ARTIST
@artists_bp.route('/<int:artist_id>', methods=['DELETE'])
@jwt_required()
def delete_artist(artist_id):
    admin_verified()
    artist = locate_record(Artist, artist_id)
    db.session.delete(artist)
    db.session.commit()
    return {}, 200

        



    