from flask import Blueprint

from init import db, ma
from models.album import Album, AlbumSchema

albums_bp = Blueprint('albums', __name__, url_prefix='/albums')

@albums_bp.route('/')
def get_cards():
    stmt = db.select(Album).order_by(Album.title)
    albums = db.session.scalars(stmt).all()
    return AlbumSchema(many=True).dump(albums)