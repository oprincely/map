from flask import Blueprint, render_template, url_for, redirect, request, session

from flask_login import current_user, login_user,login_required,logout_user
from app import db
from app.models import User,Post

import datetime

#from app.auth.forms import NumberOfQuestions,AskQuestions

x = datetime.datetime.now()
year_now = x.year


bp = Blueprint('users', __name__)

@bp.route('/users')
def users():
    user = {'username': 'Princely'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('users/users.html', user=user,posts=posts)