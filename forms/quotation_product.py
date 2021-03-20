from wtforms import BooleanField, StringField, FloatField, SubmitField, IntegerField, validators
from flask_wtf import FlaskForm

class QuotationProductForm(FlaskForm):
	quantity = IntegerField('Quantity', [validators.required(), validators.NumberRange(1, 100)])
	distance = FloatField('Distance', [validators.required(), validators.NumberRange(1, 1000)])
	quote = SubmitField('Calculer')
	buy = SubmitField('Acheter')
