from datetime import datetime, timezone

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db, ma
from models.artist import Artist, ArtistSchema
from utilities import admin_verified

artists_bp = Blueprint('artists', __name__, url_prefix='/artists')

# READ ALL ARTISTS:
@artists_bp.route('/')
def get_artists():
    stmt = db.select(Artist)
    artists = db.session.scalars(stmt)
    return ArtistSchema(many=True).dump(artists)

# READ ONE ARTIST:
@artists_bp.route('/<int:artist_id>')
@jwt_required()
def get_one_artist(artist_id):
    
    stmt = db.select(Artist).filter_by(id=artist_id)
    artist = db.session.scalar(stmt)
    if artist:
        return ArtistSchema().dump(artist)
    else:
        return {'error': 'Artist not found'}, 404

# CREATE

@artists_bp.route('/', methods=['POST'])
@jwt_required()
def create_artist():
    admin_verified()
    try:
        artist_req = ArtistSchema().load(request.json)

        artist = Artist(
                name=artist_req['name'],
                albums=artist_req.get('albums', []),
                date_created=datetime.now(timezone.utc),
                last_updated=datetime.now(timezone.utc)
                )

        db.session.add(artist)
        db.session.commit()
        return ArtistSchema().dump(artist), 201
    except:
        return {"error": "New artist must have a valid name"}

@artists_bp.route('/<int:artist_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_artist(artist_id):
    admin_verified()
    stmt = db.select(Artist).filter_by(id=artist_id)
    artist = db.session.scalar(stmt)
    if artist:
        try:
            artist_req = ArtistSchema().load(request.json)

            artist.name=artist_req.get('name', artist.name)
            artist.last_updated=datetime.now(timezone.utc)
                    
            db.session.add(artist)
            db.session.commit()
            return ArtistSchema(exclude=['albums']).dump(artist) 
        except:
            return {"error": ""}
        
    else:
        return {'erorr': 'Artist not found'}, 404

# DELETE ARTIST
@artists_bp.route('/<int:artist_id>', methods=['DELETE'])
@jwt_required()
def delete_artist(artist_id):
    admin_verified()
    stmt = db.select(Artist).filter_by(id=artist_id)
    artist = db.session.scalar(stmt)
    if artist:
        db.session.delete(artist)
        db.session.commit()
        return {}, 200
    else:
        return {"error": "Artist not found"}, 404

        



    