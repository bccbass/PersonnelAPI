from datetime import date
from time import time
# from init import bcrypt

from flask import Blueprint

from init import db, ma, jwt, bcrypt
from utilities import generate_pw
from models.album import Album
from models.musician import Musician
from models.track import Track
from models.user import User
from models.track_musician import Track_Musician

cli_commands = Blueprint('db', __name__)

@cli_commands.cli.command('create')
def create_tables():
    db.drop_all()
    db.create_all([Musician, Track, Track_Musician])
    print('Created Personnel tables')

# @cli_commands.cli.command('seed_tables' __name__)
# def seed_tables():

@cli_commands.cli.command('seed_users')
def seed_users():
    users = [
        User(
        name = "Personnel Dev",
        email = "dev@cs.com",
        password = generate_pw('dev'),
        is_admin = True,
        date_created = int(time()),
        date_updated = int(time())
        ),
        User(
        name = "Julian Adderly",
        email = "alto@cannonball.com",
        password = generate_pw('soul'),
        is_admin = False,
        date_created = int(time()),
        date_updated = int(time())
        )
    ]

    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()
    print('Succesfully seeded users!')


    
