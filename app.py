from os import environ

from flask import Flask
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_commands

def create_app():
    # create instance of Flask object
    app = Flask(__name__)

    # FLASK CONFIGURATION
    # set database location with a DB URI
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
    # JWT secret key
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')

    # Pass in app object to all instances of modules
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints with App object
    app.register_blueprint(cli_commands)

    @app.route('/')
    def index():
        return 'HI'
    return app

