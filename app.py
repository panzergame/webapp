from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

import mangopay

import os

from pages.product import product_page
from pages.auth import auth_page

from core.client import Client
from core.seller import Seller, init_seller
import core.clientgraphql as clientgraphql

app = Flask(__name__)
app.config.from_pyfile(os.environ.get('WEBAPP_CONFIG') or 'config/default.cfg')

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = b'x\xfa\xd4\x04x]g,(t\xb5\xf7j\xb9\x8c\x13'

clientgraphql.init_graphql(app)

mangopay.client_id = app.config['MANGOPAY_CLIENT_ID']
mangopay.apikey = app.config['MANGOPAY_API_KEY']

init_seller(app)

# Flask-Bootstrap requires this line
Bootstrap(app)

app.register_blueprint(product_page)
app.register_blueprint(auth_page)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login_client'


@login_manager.user_loader
def load_user(user_id):
	return Client.get(user_id)


if __name__ == '__main__':
	app.run(port=5001, debug=True)
