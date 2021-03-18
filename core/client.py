from flask_login import UserMixin

from mangopay.api import APIRequest
from mangopay.resources import *
from mangopay.utils import Address

from gql import gql
from . import clientgraphql

class Client(UserMixin):
	def __init__(self, id, username, email, mangopayid=None):
		self.id = id
		self.username = username
		self.email = email
		
		if mangopayid:
			self.__mangopay_user = Client.get(mangopayid)

	def register_mangopay(self, firstname, lastname, birthday, nationality, country_of_residence):
		self.__mangopay_user = NaturalUser(
						first_name=firstname,
						last_name=lastname,
						birthday=birthday,
						nationality=nationality,
						country_of_residence=country_of_residence,
						email=self.email)
		self.__mangopay_user.save()

		self.save()

	@staticmethod
	def create(username, email, password):
		query = gql('''mutation {{
	registerClient(username: "{}", email: "{}", password: "{}") {{
		id
	}}
}}'''.format(username, email, password))

		result = clientgraphql.clientql.execute(query)
		id = result['registerClient']['id']

		user = Client(id, username, email)
		return user

	@staticmethod
	def get(id):
		query = gql('''{{
	client (id: "{}"){{
		id,
		username,
		email
	}}
}}'''.format(id))

		result = clientgraphql.clientql.execute(query)
		data = result['client']
		return Client(data['id'], data['username'], data['email'])

	@staticmethod
	def get_by_credential(email, password):
		return Client(0, 'toto', email, password)  # TODO

