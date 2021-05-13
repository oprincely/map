from flask import render_template, flash, redirect, url_for, Blueprint, url_for, redirect, request, session

############### Microblog things
from app.models import User,Post
from app import db
from .forms import LoginForm,RegistrationForm
from flask_login import current_user, login_user,logout_user,login_required 
 
from werkzeug.urls import url_parse
import datetime

from .forms import ResetPasswordForm,ResetPasswordRequestForm
from .email import send_password_reset_email
################################

x = datetime.datetime.now()
year_now = x.year

bp = Blueprint('auth', __name__)

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('users.users'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html',title='Reset Password', form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('users.users'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('users.users'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.profile')
        return redirect(next_page)
    
    return render_template('auth/login1.html', title='Sign In', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,middlename=form.middlename.data,lastname=form.lastname.data,
                    dob=form.dob.data,tob=form.tob.data,pob=form.pob.data,mobile=form.mobile.data,number_of_questions=1,
                    username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        #msg = 'Congratulations, you are now a registered user!'
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register1.html', form=form) 

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))