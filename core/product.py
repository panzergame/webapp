from gql import gql
from . import clientgraphql

class Product:
	def __init__(self, title, description, cost, weight):
		self.title = title
		self.description = description
		self.cost = cost
		self.weight = weight

	@staticmethod
	def get(id):
		pass

	def get_all():
		pass
