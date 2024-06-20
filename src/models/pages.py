from src.database.connection import db
from sqlalchemy.orm import relationship
class Page (db.Model):
    __tablename__ = "pages"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = relationship("User   ")