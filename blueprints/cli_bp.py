
from flask import Blueprint

from init import db, ma, jwt
from blueprints.seed_data import users, albums, musicians, tracks
from models.album import Album
from models.musician import Musician
from models.track import Track
from models.user import User
from models.track_musician import track_musician

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
    # Albums
    db.session.query(Album).delete()
    db.session.add_all(albums)
    db.session.commit()
    print('Seeded albums')    
    # Tracks
    tracks[0].musicians.append(musicians[0])

    for i in range(len(tracks)):
        db.session.add_all(tracks[i])
    db.session.commit()
    print('Seeded tracks')    
    # Musicians
    db.session.query(Musician).delete()
    db.session.add_all(musicians)
    db.session.commit()
    print('Seeded musicians')  
    

    
