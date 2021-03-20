from wtforms import BooleanField, StringField, FloatField, SubmitField, IntegerField, DateField, validators
from flask_wtf import FlaskForm

class BuyProductForm(FlaskForm):
	number = StringField('Number')
	cvx = StringField('CVX')
	expiration_date = DateField('Expiration Date', format='%m/%y')
	first_name = StringField('First Name')
	last_name = StringField('Last Name')
	birthday = DateField('Birthday', format='%d/%m/%Y')
	submit = SubmitField('Acheter')
