from flask import session, redirect
from functools import wraps

def unauthenticated_only (f):
    @wraps(f)
    def wrapper (*args, **kwards):
        if "user" in session:
            return redirect("/dashboard")
        else:
            return f(*args, **kwards)
    return wrapper

def authenticated_only (f):
    @wraps(f)
    def wrapper (*args, **kwards):
        if "user" not in session:
            return redirect("/")
        else:
            return f(*args, **kwards)
    return wrapper