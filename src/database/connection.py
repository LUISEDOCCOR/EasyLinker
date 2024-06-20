from app import app
import os
from flask_sqlalchemy import SQLAlchemy


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DBNAME = os.getenv("POSTGRES_DBNAME")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 