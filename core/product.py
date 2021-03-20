from gql import gql
from . import clientgraphql

from .quote import Quote

from money.money import Money
from money.currency import Currency

class Product:
	def __init__(self, id='', title='', description='', cost='', weight=''):
		self.id = id
		self.title = title
		self.description = description
		self.cost = Money(cost, Currency.EUR)
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

	def quote(self, distance, quantity):
		product_cost = self.cost * quantity
		total_weight = self.weight * quantity
		shipping_cost = self._shipping_cost(distance, total_weight)
		total_cost = product_cost + shipping_cost

		return Quote(product_cost=product_cost, total_weight=total_weight, shipping_cost=shipping_cost, total_cost=total_cost, distance=distance, quantity=quantity)

	def _shipping_cost(self, distance, total_weight):
		#print(distance * total_weight)
		return Money('4.3', Currency.EUR)  # TODO wsdl
