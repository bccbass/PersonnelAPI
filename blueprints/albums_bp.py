from datetime import datetime, timezone

from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required

from init import db, ma
from models.album import Album, AlbumSchema
from models.artist import Artist, ArtistSchema
from utilities import admin_verified, locate_record, preexisting_record

albums_bp = Blueprint('albums', __name__, url_prefix='/albums')

# GET ALL ALBUMS:
@albums_bp.route('/')
@jwt_required()
def get_albums():
    stmt = db.select(Album)
    albums = db.session.scalars(stmt).all()
    return AlbumSchema(many=True, exclude=['tracks']).dump(albums)

# GET ONE ALBUM:
@albums_bp.route('/<int:album_id>')
def get_one_album(album_id):
    album = locate_record(Album, album_id)
    return AlbumSchema(exclude=['artist_id']).dump(album)

    
# CREATE A NEW ALBUM:
@albums_bp.route('/', methods=['POST'])
@jwt_required()
def create_album():
    admin_verified()
    album_req = AlbumSchema().load(request.json)

    # CHECK ALBUM DOES NOT EXIST:
    stmt = db.select(Album).filter_by(title=album_req['title'], artist_id=album_req['artist_id'])
    preexisting_record(stmt)

    album = Album(
        title=album_req['title'],
        artist_id=album_req['artist_id'],
        release_date=album_req.get('release_date', None),
        img_url=album_req.get('img_url', None),
        date_created= datetime.now(timezone.utc),
        last_updated= datetime.now(timezone.utc)
    )

    db.session.add(album)
    stmt = db.select(Album).filter_by(title=album.title, artist_id=album.artist_id)

    # preexisting_record(stmt)

    db.session.commit()
    return AlbumSchema(exclude=['artist_id']).dump(album)

# UPDATE ALBUM
@albums_bp.route('/<int:album_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_album(album_id):
    admin_verified()
    album_req = AlbumSchema().load(request.json)
    album = locate_record(Album, album_id)
        
    album.title = album_req.get('title', album.title)
    album.artist = album_req.get('artist', album.artist)
    album.release_date = album_req.get('release_date', album.release_date)
    album.img_url = album_req.get('img_url', album.img_url)
    album.date_created = album.date_created
    album.last_updated = datetime.now(timezone.utc)
            

    db.session.add(album)
    db.session.commit()
    return AlbumSchema().dump(album)


# DELETE ALBUM
@albums_bp.route('/<int:album_id>', methods=['DELETE'])
@jwt_required()
def delete_album(album_id):
    admin_verified()
    album = locate_record(Album, album_id)
    db.session.delete(album)
    db.session.commit()
    return {'Message': f'Album with title <{album.title}> and id <{album_id}> succesfully deleted!'}, 200
