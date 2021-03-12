from flask import Blueprint, render_template

main_page = Blueprint('main', __name__)

@main_page.route('/')
def index():
    return render_template('index.html')
