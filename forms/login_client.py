from wtforms import BooleanField, StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm

class LoginClientForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])
    submit = SubmitField('Submit')
    remember = BooleanField('Remember')
