from flask import Blueprint, render_template, redirect, url_for
from forms.register_client import RegisterClientForm
from forms.login_client import LoginClientForm
from flask_login import login_user, login_required

from core.client import Client

auth_page = Blueprint('auth', __name__)

@auth_page.route('/client/register', methods=['GET', 'POST'])
def register_client():
    form = RegisterClientForm()
    if form.validate_on_submit():
        print(form)
        client = Client.create(form.username, form.email, form.password)
        
        return redirect(url_for('auth.login_client'))

    return render_template('register_client.html', form=form)

@auth_page.route('/client/login', methods=['GET', 'POST'])
def login_client():
    form = LoginClientForm()
    if form.validate_on_submit():
        client = Client.get_by_credential(form.email, form.password)
        login_user(client, remember=form.remember)

        return redirect(url_for('main.client_profile'))

    return render_template('login_client.html', form=form)
