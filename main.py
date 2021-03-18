from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_page = Blueprint('main', __name__)

@main_page.route('/')
def index():
    return render_template('index.html')

@main_page.route('/products')
@login_required
def products():
    return render_template('products.html', name=current_user.username)
