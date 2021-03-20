from gql import gql
from . import clientgraphql
from .quote import Quote

class Product:
	def __init__(self, id='', title='', description='', cost='', weight=''):
		self.id = id
		self.title = title
		self.description = description
		self.cost = float(cost)
		self.weight = float(weight)

	@staticmethod
	def get(id):
		query = gql('''{{
	product (id: "{}"){{
		id,
		title,
		description,
		cost,
		weight
	}}
}}'''.format(id))

		result = clientgraphql.clientql.execute(query)
		return Product(**result['product'])

	@staticmethod
	def get_all():
		query = gql('''{
	products {
		id,
		title,
		description,
		cost,
		weight
	}
}''')

		result = clientgraphql.clientql.execute(query)
		return [Product(**data) for data in result['products']]

	def quantity_cost(self, quantity):
		return self.cost * quantity

	def shipping_cost(self, distance, quantity):
		return distance  # WSDL
