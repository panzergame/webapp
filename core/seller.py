from flask_login import UserMixin

from mangopay.api import APIRequest
from mangopay.resources import *
from mangopay.utils import Address

from gql import gql
from . import clientgraphql
import requests


class Seller():
	def __init__(self, mangopayid):
		self.mangopay_user = NaturalUser.get(mangopayid)
		self.wallet = self.mangopay_user.wallets[0]


seller = None


def init_seller(app):
	global seller
	seller = Seller(app.config['MANGOPAY_SELLER_ID'])
