from flask import Blueprint, render_template, redirect, url_for
from forms.register_client import RegisterClientForm
from forms.login_client import LoginClientForm
from flask_login import login_user, login_required, logout_user

from core.client import Client

auth_page = Blueprint('auth', __name__)

@auth_page.route('/client/register', methods=['GET', 'POST'])
def register_client():
	form = RegisterClientForm()
	if form.validate_on_submit():
		client = Client.create(form.username.data, form.email.data, form.password.data)
		login_user(client)

		return redirect(url_for('product.products'))

	return render_template('register_client.html', form=form)


@auth_page.route('/client/login', methods=['GET', 'POST'])
def login_client():
	form = LoginClientForm()
	if form.validate_on_submit():
		client = Client.get_by_credential(form.email.data, form.password.data)
		login_user(client, remember=form.remember.data)

		return redirect(url_for('product.products'))

	return render_template('login_client.html', form=form)


@auth_page.route('/client/logout', methods=['GET', 'POST'])
@login_required
def logout_client():
	logout_user()
	return redirect(url_for('product.products'))
