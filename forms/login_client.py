from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm

class LoginClientForm(FlaskForm):
    email = StringField('Email Address', [validators.required()])
    password = PasswordField('Password', [validators.required()])
    remember = BooleanField('Remember')
    submit = SubmitField('Submit')
