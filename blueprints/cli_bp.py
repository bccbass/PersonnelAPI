
from flask import Blueprint

from init import db, ma, jwt
from blueprints.seed_data import users, artists, albums, instruments, musicians, tracks, track_musicians
from models.artist import Artist
from models.album import Album
from models.instrument import Instrument
from models.musician import Musician
from models.track import Track
from models.user import User
from models.track_musician import Track_Musician

cli_commands = Blueprint('db', __name__)

@cli_commands.cli.command('create')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Created Personnel tables')

@cli_commands.cli.command('seed_users')
def seed_users():
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()
    print('Succesfully seeded users')


@cli_commands.cli.command('seed_tables')
def seed_tables():
    # ARTISTS
    db.session.query(Artist).delete()
    db.session.add_all(artists)
    db.session.commit()
    print('Succesfully seeded artists')

    # Albums
    db.session.query(Album).delete()
    db.session.add_all(albums)
    db.session.commit()
    print('Seeded albums')

    # Tracks
    db.session.query(Track).delete()
    db.session.add_all(tracks)
    db.session.commit()
    print('Seeded tracks')    

    # Instruments
    db.session.query(Instrument).delete()
    db.session.add_all(instruments)
    db.session.commit()
    print('Seeded instruments')  

    # Musicians
    db.session.query(Musician).delete()
    db.session.add_all(musicians)
    db.session.commit()
    print('Seeded musicians')  

    #  Track_Musicians
    db.session.query(Track_Musician).delete()
    db.session.add_all(track_musicians)
    db.session.commit()
    print('Seeded track_musicians')  
    

    
@cli_commands.cli.command('query')
def query():
    tracks = Track.query.all()
    musicians = Musician.query.all()

    print(tracks[0], tracks[0].album, tracks[0].musicians)
    print(musicians[7], musicians[7].tracks)