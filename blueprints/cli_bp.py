
from flask import Blueprint

from init import db, ma, jwt
from blueprints.seed_data import users, albums, musicians, tracks
from models.album import Album
from models.musician import Musician
from models.track import Track
from models.user import User
# from models.track_musician import Track_Musician

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
    # tracks[0].musicians.append(musicians[0])

    for i in range(len(tracks)):
        db.session.add_all(tracks[i])
    db.session.commit()
    print('Seeded tracks')    
    # Musicians
    db.session.query(Musician).delete()
    db.session.add_all(musicians)
    db.session.commit()
    print('Seeded musicians')  



@cli_commands.cli.command('create_associations')
def create_associations():
    stmt = db.select(Track)
    tracks = db.session.scalars(stmt)
    stmt2 = db.select(Musician).filter_by(l_name='Davis')
    stmt3 = db.select(Musician).filter_by(l_name='Shorter')
    miles = db.session.scalar(stmt2)
    wayne = db.session.scalar(stmt3)
    print(wayne)

    
    miles.tracks.extend(tracks)
    wayne.tracks.extend(tracks)
    db.session.commit()
   
    tracks = Track.query.all()
    musicians = Musician.query.all()

    print('Track1 musicians', tracks[0].musicians)
    print(musicians[1].tracks)
    # # Track_Musician
    # db.session.query(Track_Musician).delete()
    # db.session.add_all(track_musicians)
    # db.session.commit()
    # print('Seeded track_musicians')  
    

    
