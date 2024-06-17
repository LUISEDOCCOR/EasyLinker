from src.database.connection import db

class User (db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

