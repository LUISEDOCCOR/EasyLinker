from flask import Blueprint, render_template, redirect, sessions
from src.decorators.auth import authenticated_only


dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard")
@authenticated_only
def dashboard():
    return render_template("/pages/dashboard.html")