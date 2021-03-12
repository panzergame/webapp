from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from main import main_page
from auth import auth_page

from core.client import Client

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = b'x\xfa\xd4\x04x]g,(t\xb5\xf7j\xb9\x8c\x13'

# Flask-Bootstrap requires this line
Bootstrap(app)

app.register_blueprint(main_page)
app.register_blueprint(auth_page)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Client.get(user_id)
