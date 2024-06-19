from flask import session, redirect, url_for
from functools import wraps


def unauthenticated_only(f):
    @wraps(f)
    def wrapper(*args, **kwards):
        if "user" in session:
            return redirect(url_for("dashboard.home"))
        else:
            return f(*args, **kwards)

    return wrapper


def authenticated_only(f):
    @wraps(f)
    def wrapper(*args, **kwards):
        if "user" not in session:
            return redirect(url_for("index"))
        else:
            return f(*args, **kwards)

    return wrapper
