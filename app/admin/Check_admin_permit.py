from functools import wraps

from flask import Blueprint,session #flash,render_template, url_for, redirect, request,
from flask_login import current_user
import os
from app.models import User

def check_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = current_user.username
        user = User.query.filter_by(username=username).first()
        if user.username == 'admin' and user.email == os.environ.get('ADMINS'):
            return func(*args, **kwargs)
        return "<p>This is the END of the INTERNET, please NOTHING IS HERE.</p>"
    return wrapper
