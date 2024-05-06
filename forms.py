# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class AvailabilityForm(FlaskForm):
    start_time = DateTimeField('Start Time', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    end_time = DateTimeField('End Time', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    submit = SubmitField('Submit')