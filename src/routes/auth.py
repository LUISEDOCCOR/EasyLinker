from flask import Blueprint, render_template, request, redirect, session, jsonify
from src.database.connection import db
from src.models.users import User
from src.lib.bcrypt import createPassword, chechPassword
from src.decorators.auth import unauthenticated_only

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["GET", "POST"])
@unauthenticated_only
def signup():

    error = None

    if request.method == "POST":
        currentUsername = request.form["username"]
        currentEmail = request.form["email"]
        currentPassword = request.form["password"]

        if (
            len(currentUsername) > 3
            and len(currentEmail) > 3
            and len(currentPassword) > 3
        ):

            existing_user = User.query.filter_by(email=currentEmail).first()

            hashPassword = createPassword(currentPassword)

            if existing_user is None:
                user = User(
                    name=currentUsername, email=currentEmail, password=hashPassword
                )
                db.session.add(user)
                db.session.commit()

                session["user"] = {
                    "name": user.name,
                    "email": user.email,
                    "id": user.id,
                }

                return redirect("/dashboard")
            else:
                error = "El correo ya existe"
        else:
            error = "Cada campo debe de tener mínimo 3 caracteres"

    # method == GET
    inputs = [
        {
            "name": "username",
            "placeholder": "Nombre",
            "type": "text",
            "color": "pastelPink",
        },
        {
            "name": "email",
            "placeholder": "Correo",
            "type": "email",
            "color": "pastelOrange",
        },
        {
            "name": "password",
            "placeholder": "Contraseña",
            "type": "text",
            "color": "pastelBlue",
        },
    ]
    return render_template(
        "/pages/auth.html",
        inputs=inputs,
        bottomMessage="Ya tienes cuenta, inicia sesión aquí",
        bottomLink="auth.login",
        error=error,
    )


@auth_bp.route("/login", methods=["GET", "POST"])
@unauthenticated_only
def login():

    error = None

    if request.method == "POST":
        currentEmail = request.form["email"]
        currentPassword = request.form["password"]

        if len(currentEmail) > 3 and len(currentPassword) > 3:

            user = User.query.filter_by(email=currentEmail).first()

            if user:
                password_is_correct = chechPassword(
                    passwordHashed=user.password, userPassword=currentPassword
                )
                if password_is_correct:
                    session["user"] = {
                        "name": user.name,
                        "email": user.email,
                        "id": user.id,
                    }
                    return redirect("/dashboard")
                else:
                    error = "El usuario no existe"

            else:
                error = "El usuario no existe"
        else:
            error = "Cada campo debe de tener mínimo 3 caracteres"

    inputs = [
        {
            "name": "email",
            "placeholder": "Correo",
            "type": "email",
            "color": "pastelOrange",
        },
        {
            "name": "password",
            "placeholder": "Contraseña",
            "type": "text",
            "color": "pastelBlue",
        },
    ]
    return render_template(
        "/pages/auth.html",
        inputs=inputs,
        bottomMessage="No tienes cuenta, crea una aquí",
        bottomLink="auth.signup",
        error=error,
    )


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")
