from flask_login import UserMixin

from mangopay.api import APIRequest
from mangopay.resources import *
from mangopay.utils import Address

from gql import gql
from . import clientgraphql
from . import seller
import requests


class Client(UserMixin):
	def __init__(self, id='', username='', email=''):
		self.id = id
		self.username = username
		self.email = email

	def _register_mangopay(self, firstname, lastname, birthday, nationality, country_of_residence):
		print(self.id)
		self.mangopay_user = NaturalUser(
						first_name=firstname,
						last_name=lastname,
						birthday=int(birthday.strftime('%s')),
						nationality=nationality,
						country_of_residence=country_of_residence,
						email=self.email)
		self.mangopay_user.save()

	def _register_card(self, number, cvx, expiration_date):
		card_registration = CardRegistration(user=self.mangopay_user, currency='EUR')
		card_registration.save()

		tokenizer_url = card_registration.card_registration_url
		res = requests.post(
			tokenizer_url, data={
				'cardNumber': number,
				'cardCvx': cvx,
				'cardExpirationDate': expiration_date.strftime('%m%y'),
				'accessKeyRef': card_registration.access_key,
				'data': card_registration.preregistration_data
			})

		card_registration.registration_data = res.text
		card_registration.save()
		self.card = card_registration.card

	def buy_product(
			self, product, quote, number, cvx, expiration_date, first_name,
			last_name, birthday):

		self._register_mangopay(first_name, last_name, birthday, 'FR', 'FR')
		self._register_card(number, cvx, expiration_date)

		direct_payin = DirectPayIn(
				author=self.mangopay_user,
				debited_funds=Money(amount=quote.total_cost.sub_units, currency='EUR'),
				fees=Money(amount=0, currency='EUR'),
				credited_wallet_id=seller.seller.wallet,
				card_id=self.card,
				secure_mode="DEFAULT",
				secure_mode_return_url="https://www.ulule.com/")

		direct_payin.save()

	@staticmethod
	def create(username, email, password):
		query = gql('''mutation {{
	registerClient(username: "{}", email: "{}", password: "{}") {{
		id
	}}
}}'''.format(username, email, password))

		result = clientgraphql.client.execute(query)
		id = result['registerClient']['id']

		return Client(id=id, username=username, email=email)

	@staticmethod
	def get(id):
		query = gql('''{{
	clientById (id: "{}"){{
		id,
		username,
		email
	}}
}}'''.format(id))

		result = clientgraphql.client.execute(query)
		return Client(**result['clientById'])

	@staticmethod
	def get_by_credential(email, password):
		query = gql('''{{
	clientByCredential (email: "{}", password: "{}"){{
		id,
		username,
		email
	}}
}}'''.format(email, password))

		result = clientgraphql.client.execute(query)
		return Client(**result['clientByCredential'])
