from flask import Blueprint, flash,render_template, url_for, redirect, request, session

from flask_login import current_user, login_user,login_required,logout_user
from app import db
from app.models import User,Post
from app.auth.forms import EditProfileForm,PostForm
import os
from datetime import datetime

#from app.auth.forms import NumberOfQuestions,AskQuestions


bp = Blueprint('users', __name__)
'''
@bp.route('/users', methods=['GET', 'POST'])
#@login_required
def users():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        
        flash('Your post is now live!')
        return redirect(url_for('users.users'))
    
    posts = Post.query.all()
    #posts = current_user.followed_posts().all()
    return render_template("users/users.html", title='Users Page', form=form,posts=posts)
'''
@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('users/user.html', user=user, posts=posts)

'''
@bp.route('/user/<username>/popup')
@login_required
def user_popup(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = EmptyForm()
    return render_template('users/user_popup.html', user=user, form=form)

'''
@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('users.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('users/edit_profile.html', title='Edit Profile',form=form)

'''
@bp.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    return render_template("users.explore.html", title='Explore', posts=posts.items)

'''
@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()