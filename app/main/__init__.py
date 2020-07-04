from flask import Blueprint #, render_template, url_for, redirect, request, session

import datetime

x = datetime.datetime.now()
year_now = x.year


bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return "this is my app"