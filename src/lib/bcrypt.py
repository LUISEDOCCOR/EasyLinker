from flask_bcrypt import Bcrypt
from app import app

bcrypt = Bcrypt(app)


def createPassword(password):
    passwordhashed = bcrypt.generate_password_hash(password).decode("utf-8")
    return passwordhashed


def chechPassword(passwordHashed, userPassword):
    result = bcrypt.check_password_hash(passwordHashed, userPassword)
    return result
