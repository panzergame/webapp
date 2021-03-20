from gql import gql
from . import clientgraphql
from . import clientsoap

from .quote import Quote

from money.money import Money
from money.currency import Currency

from decimal import Decimal

class Product:
	def __init__(self, id='', title='', description='', cost='', weight=''):
		self.id = id
		self.title = title
		self.description = description
		self.cost = Money(cost, Currency.EUR)
		self.weight = Decimal(weight)

	@staticmethod
	def get(id):
		query = gql('''{{
	productById (id: "{}"){{
		id,
		title,
		description,
		cost,
		weight
	}}
}}'''.format(id))

		result = clientgraphql.client.execute(query)
		return Product(**result['productById'])

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

		result = clientgraphql.client.execute(query)
		return [Product(**data) for data in result['products']]

	def quote(self, distance, quantity):
		product_cost = self.cost * quantity
		total_weight = self.weight * quantity
		shipping_cost = self._shipping_cost(distance, total_weight)
		total_cost = product_cost + shipping_cost

		return Quote(product_cost=product_cost, total_weight=total_weight, shipping_cost=shipping_cost, total_cost=total_cost, distance=distance, quantity=quantity)

	def _shipping_cost(self, distance, total_weight):
		shipping_cost = clientsoap.client.service.compute_shipping_cost(distance, total_weight)
		print(total_weight, distance, shipping_cost)
		return Money(shipping_cost, Currency.EUR)
