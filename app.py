from flask import Flask
import os
from datetime import timedelta
from dotenv import load_dotenv


load_dotenv()

app = Flask(
    __name__, 
    template_folder="./src/templates",
    static_folder="./src/static"
)
app.secret_key = os.getenv("APP_KEY")
app.config["PERMANENT_SESSION_LIFETIME"]=timedelta(days=7)

