from flask import abort

from flask_jwt_extended import get_jwt_identity

from init import bcrypt, db
from models.user import User

def generate_pw(raw_password):
    return bcrypt.generate_password_hash(raw_password).decode("utf8")

def admin_verified():
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)

    if not (user and user.is_admin):
        abort(401, description="Invalid credentials")