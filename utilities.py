from init import bcrypt 

def generate_pw(raw_password):
    return bcrypt.generate_password_hash(raw_password).decode("utf8")