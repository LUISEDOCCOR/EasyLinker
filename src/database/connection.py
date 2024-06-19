from app import app
import os
from flask_sqlalchemy import SQLAlchemy


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PORT = "4321"
POSTGRES_HOST = "localhost"
POSTGRES_DBNAME = "sqlalchemy"

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{POSTGRES_USER}:54321@localhost:4321/sqlalchemy" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 