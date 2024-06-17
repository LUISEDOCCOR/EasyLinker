from flask import Blueprint, render_template, request, redirect
from src.database.connection import db
from src.models.users import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/signup", methods = ["GET", "POST"])
def signup ():

    error = None

    if request.method == "POST":
        currentUsername = request.form["username"]
        currentEmail = request.form["email"]
        currentPassword = request.form["password"]

        if(
            len(currentUsername) > 3 and
            len(currentEmail) > 3 and
            len(currentPassword) > 3 
        ):  

            existing_user = User.query.filter_by(email=currentEmail).first()

            if(existing_user is None):    
                user = User(name=currentUsername, email=currentEmail, password=currentPassword)
                db.session.add(user)
                db.session.commit()
                return redirect("/")
            else:
                error = "El correo ya existe"
            
        else:
            error = "Rellene todos los campos"
        
    
    inputs = [
        {"name": "username", "placeholder": "Nombre", "type":"text", "color": "pastelPink"},
        {"name": "email", "placeholder": "Correo", "type":"email", "color": "pastelOrange"},
        {"name": "password", "placeholder": "Contraseña", "type":"text", "color": "pastelBlue"}
    ]
    return render_template("/pages/signup.html", inputs=inputs, error = error)
