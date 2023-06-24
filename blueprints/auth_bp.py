from datetime import timedelta, datetime, timezone

from flask import request, Blueprint, abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from init import db, bcrypt
from models.user import User, UserSchema
from utilities import generate_pw, admin_verified 





auth_bp = Blueprint('auth', __name__, url_prefix=('/users'))

@auth_bp.route('/register', methods=['POST'])
def register_user():
    try:
        user_req = UserSchema().load(request.json)
        new_user = User(
            name = user_req['name'],
            email = user_req['email'],
            password = generate_pw(user_req['password']),
            is_admin = False,
            date_created = datetime.now(timezone.utc),
            last_updated = datetime.now(timezone.utc)
        )

        db.session.query(User)
        db.session.add(new_user)
        db.session.commit()

        return UserSchema(exclude=['password', 'is_admin']).dump(new_user), 201
    except IntegrityError:
        return {'error': 'Email address already registered'}, 409
    
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        user_req = UserSchema().load(request.json)
        stmt = db.select(User).filter_by(email=user_req['email'])
        user = db.session.scalar(stmt)

        if user and bcrypt.check_password_hash(user.password, user_req['password']):
            token = create_access_token(identity=user.id, expires_delta=timedelta(days=30))
            print(token)
            return {'user': user.name, 'token': token} 
        else:
            return {"error": "Invalid email or password" }, 401
    except KeyError:
        return {'error': "Email and Password required"}, 401
    
@auth_bp.route('/grant_admin_access/<int:user_id>', methods=['POST'])
@jwt_required()
def grant_admin_access(user_id):
    admin_verified()
    stmt = db.select(User).filter_by(id = user_id)
    user = db.session.scalar(stmt)

    if user:
        user.is_admin = True
        user.last_updated = datetime.now(timezone.utc)
        db.session.commit()
        return UserSchema().dump(user)
    else:
        return {'error': 'User not found'}, 404
    
@auth_bp.route('/')
def show_all_users():
    admin_verified()
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    
    return UserSchema(many=True, exclude=['password']).dump(users)

