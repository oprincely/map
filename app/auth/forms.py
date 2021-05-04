#from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, BooleanField, SubmitField
#from wtforms.validators import DataRequired

class NumberOfQuestions(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    numberofquestions = StringField('Numberofquestions', validators=[DataRequired()])
    submit = SubmitField('Update')
    

class AskQuestions(FlaskForm):
    question = TextAreaField('Ask Your Question', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Ask')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    

class RegistrationForm(FlaskForm):
    firstname = StringField('Fisrtname', validators=[DataRequired()])
    middlename = StringField('Middlename')
    lastname = StringField('Lastname', validators=[DataRequired()])
    dob = StringField('Date of birth: 22/02/2020', validators=[DataRequired()])
    tob = StringField('Time of birth: 1/24 am and n for unknown', validators=[DataRequired()])
    pob = StringField('Place, State, and Country of birth', validators=[DataRequired()])
    mobile = StringField('Mobile Number', validators=[DataRequired()])
    
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
class PredictionForm(FlaskForm):
    firstname = StringField('Fisrtname', validators=[DataRequired()])
    middlename = StringField('Middlename')
    lastname = StringField('Lastname', validators=[DataRequired()])
    dob = StringField('Date of birth: 22/02/2020', validators=[DataRequired()])
    year = StringField('Year in past: 2020')
    submit = SubmitField('Predict')
    
class RelationshipForm(FlaskForm):
    firstname = StringField('Fisrtname', validators=[DataRequired()])
    middlename = StringField('Middlename')
    lastname = StringField('Lastname', validators=[DataRequired()])
    dob = StringField('Date of birth: 22/02/2020', validators=[DataRequired()])
    
    firstname1 = StringField('Partiners Fisrtname', validators=[DataRequired()])
    middlename1 = StringField('Partiners Middlename')
    lastname1 = StringField('Partiners Lastname', validators=[DataRequired()])
    dob1 = StringField('Partiners Date of birth: 22/02/2020', validators=[DataRequired()])
    
    year = StringField('Year in past: 2020')
    submit = SubmitField('Read Relationship')
        
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
    
class PostForm(FlaskForm):
    post = TextAreaField('Enter Your Question here...', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Ask Question')
    
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
    
class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[
        DataRequired(), Length(min=0, max=140)])
    submit = SubmitField('Submit')