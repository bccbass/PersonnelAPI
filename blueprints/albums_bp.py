from flask import Blueprint

from init import db
from models.album import Album

albums_bp = Blueprint('albums', __name__, url_prefix='/cards')

@albums_bp.route('/')
def get_cards():
    stmt = db.select(Album).order_by(Album.title)
    albums = db.session.scalars(stmt).all()
    print(albums)
    return {}