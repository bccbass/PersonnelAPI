from flask import abort

from flask_jwt_extended import get_jwt_identity

from init import bcrypt, db
from models.user import User

# GENERATES HASHED/ENCODED PASSWORDS FROM GIVEN STRING
def generate_pw(raw_password):
    return bcrypt.generate_password_hash(raw_password).decode("utf8")

# ACCEPTS A MODEL AND RECORD ID AND ATTEMPTS TO LOCATE. 
# IF LOCATED RECORD IS RETURNED, IF NOT IT ABORTS WITH 404 ERROR
def locate_record(Model, record_id):
    stmt = db.select(Model).filter_by(id=record_id)
    record = db.session.scalar(stmt)
    if not record:
        abort(404, description=f"Requested record with id <{record_id}> does not exist.")
    else:
        return record

# ACCEPTS A SELECT STATEMENT AND LOCATES THE RECORD OR ABORTS
def locate_stmt(stmt):
    record = db.session.scalar(stmt)
    if not record:
        abort(404, description=f"Requested record does not exist.")
    else:
        return record


# VERIFYS CREDENTIALS BY EXTRACTING USER ID FROM JWT TOKEN AND QUERYING DB
# TO DETERMINE IF IS_ADMIN = TRUE, ABORTING IF IMPROPER AUTH.
def admin_verified():
    stmt = db.select(User).filter_by(id=get_jwt_identity())
    user = db.session.scalar(stmt)

    if not (user and user.is_admin):
        abort(401, description="Invalid credentials")

def preexisting_record(stmt):
    existing_album = db.session.scalar(stmt)
    if existing_album:
        abort(400, description="Record already exists")

char_value = '^[a-zA-Z0-9 ]+$'