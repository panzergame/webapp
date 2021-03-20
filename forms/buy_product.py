from wtforms import BooleanField, StringField, FloatField, SubmitField, IntegerField, DateField, validators
from flask_wtf import FlaskForm

class BuyProductForm(FlaskForm):
	number = StringField('Number', [validators.Length(16)])
	cvx = StringField('CVX', [validators.Length(3)])
	expiration_date = DateField('Expiration Date')
	first_name = StringField('First Name')
	last_name = StringField('Last Name')
	birthday = DateField('Birthday')
	submit = SubmitField('Buy')
