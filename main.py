from flask import render_template
import os
from flask_bcrypt import Bcrypt
from app import app #app FLASK
from src.routes.auth import auth_bp
from src.routes.dashboard import dashboard_bp
from src.database.connection import db
from src.decorators.auth import unauthenticated_only

with app.app_context():
    from src.models.users import User
    db.create_all()

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)


@app.route("/")
@unauthenticated_only
def index ():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=3000), debug=True)