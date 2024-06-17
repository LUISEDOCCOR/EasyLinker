from flask import render_template, jsonify
import os
from app import app #app FLASK
from src.routes.auth import auth_bp
from src.database.connection import db


with app.app_context():
    from src.models.users import User
    db.create_all()

app.register_blueprint(auth_bp)


@app.route("/")
def index ():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=3000), debug=True)