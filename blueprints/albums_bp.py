from datetime import datetime, timezone

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db, ma
from models.album import Album, AlbumSchema
from utilities import admin_verified

albums_bp = Blueprint('albums', __name__, url_prefix='/albums')

@albums_bp.route('/')
@jwt_required()
def get_albums():
    stmt = db.select(Album)
    albums = db.session.scalars(stmt).all()
    return AlbumSchema(many=True).dump(albums)

@albums_bp.route('/<int:album_id>')
def get_one_album(album_id):
    stmt = db.select(Album).filter_by(id=album_id)
    album = db.session.scalar(stmt)
    if album:
        return AlbumSchema().dump(album)
    else:
        return {'error': 'Album not found'}, 404
    
    
@albums_bp.route('/', methods=['POST'])
def create_album():
    admin_verified()
    album_req = AlbumSchema().load(request.json)

    album = Album(
        title=album_req['title'],
        artist=album_req['artist'],
        label=album_req['label'],
        release_date=album_req['release_date'],
        genre=album_req['genre'],
        img_url=album_req['img_url'],
        date_created= datetime.now(timezone.utc),
        last_updated= datetime.now(timezone.utc)
    )

    db.session.add(album)
    db.session.commit()
    return AlbumSchema().dump(album)

# UPDATE ALBUM
@albums_bp.route('/<int:album_id>', methods=['PUT', 'PATCH'])
def update_album(album_id):
    admin_verified()
    album_req = AlbumSchema().load(request.json)

    stmt = db.select(Album).filter_by(id=album_id)
    album = db.session.scalar(stmt)
    if album:
        
        album.title = album_req.get('title', album.title)
        album.artist = album_req.get('artist', album.artist)
        album.label = album_req.get('label', album.label)
        album.release_date = album_req.get('release_date', album.release_date)
        album.genre = album_req.get('genre', album.genre)
        album.img_url = album_req.get('img_url', album.img_url)
        album.date_created = album.date_created
        album.last_updated = datetime.now(timezone.utc)
            

        db.session.add(album)
        db.session.commit()
        return AlbumSchema().dump(album)
    else:
        return {'error': 'Album not found'}, 404

# DELETE ALBUM
@albums_bp.route('/<int:album_id>', methods=['DELETE'])
@jwt_required()
def delete_album(album_id):
    admin_verified()
    stmt = db.select(Album).filter_by(id=album_id)
    album = db.session.scalar(stmt)
    if album:
        db.session.delete(album)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Album not found'}, 404