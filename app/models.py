from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime,timedelta
from app import db
from flask_login import UserMixin
from app import login
from hashlib import md5
#------------- mail -----------
from time import time
import jwt
from flask import current_app

#-------api auth -----
import base64
import os
#-------api auth -----

'''The to_collection_dict() method produces a dictionary with the user collection representation,'''
class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data
#------------ for api -----------
    
class User(PaginatedAPIMixin,UserMixin, db.Model):
    
    #------------- api auth------
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    #------------- api auth------
    
    id = db.Column(db.Integer, primary_key=True)
    
    firstname = db.Column(db.String(64), index=True, unique=True)
    middlename = db.Column(db.String(64), index=True, unique=True)
    lastname = db.Column(db.String(64), index=True, unique=True)
    dob = db.Column(db.String(64), index=True, unique=True)
    tob = db.Column(db.String(64), index=True, unique=True)
    pob = db.Column(db.String(64), index=True, unique=True)
    mobile = db.Column(db.String(64), index=True, unique=True)
    number_of_questions = db.Column(db.Integer)
    
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
    
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    #---------------- mail----------------
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
    #------------- For API -------------
    #-------The to_dict() method converts a user object to a Python representation,
    #which will then be converted to JSON ---------
    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'last_seen': self.last_seen.isoformat() + 'Z',
            'about_me': self.about_me,
            'post_count': self.posts.count(),
            ##'follower_count': self.followers.count(),
            #'followed_count': self.followed.count(),
            #'_links': {
            #    'self': url_for('api.get_user', id=self.id),
            #    'followers': url_for('api.get_followers', id=self.id),
            #    'followed': url_for('api.get_followed', id=self.id),
            #    'avatar': self.avatar(128)
            #}
        }
        if include_email:
            data['email'] = self.email
        return data
    #------------- For API  -------------
    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'about_me']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])
            
    #------------- For API  -------------
    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user
    
    #------------- For API and also remove PaginatedAPIMixin, in class User(UserMixin, db.Model)-------------

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))