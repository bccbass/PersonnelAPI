from datetime import datetime, timezone

from flask import Blueprint, request
from models.album import Album, AlbumSchema

from init import db, ma
from models.album import Album, AlbumSchema

albums_bp = Blueprint('albums', __name__, url_prefix='/albums')

@albums_bp.route('/')
def get_cards():
    stmt = db.select(Album).order_by(Album.artist)
    albums = db.session.scalars(stmt).all()
    return AlbumSchema(many=True).dump(albums)

@albums_bp.route('/<album_id>')
def get_one_card(album_id):
    stmt = db.select(Album).filter_by(id=album_id)
    album = db.session.scalar(stmt)
    return AlbumSchema().dump(album)

@albums_bp.route('/', methods=['POST'])
def create_album():
    album_req = AlbumSchema().load(request.json)
    print(album_req['title'])
    # print(AlbumSchema.__dict__)
    print('DATE', datetime.now())
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
