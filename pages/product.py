from flask import Blueprint, render_template, redirect, url_for, request
from forms.quotation_product import QuotationProductForm
from forms.buy_product import BuyProductForm
from flask_login import login_user, login_required, current_user
from core.product import Product

product_page = Blueprint('product', __name__)


@product_page.route('/')
def products():
	products = Product.get_all()
	return render_template('products.html', products=products)


@product_page.route('/product/<productid>')
def product(productid):
	product = Product.get(productid)
	return render_template('product.html', product=product)


@product_page.route('/product/<productid>/quotation', methods=['GET', 'POST'])
def quotation(productid):
	product = Product.get(productid)

	form = QuotationProductForm()
	if form.validate_on_submit():
		quantity = form.quantity.data
		distance = form.distance.data

		if form.quote.data:
			quote = product.quote(distance, quantity)
			return render_template('quotation.html', form=form, product=product, quote=quote)
		elif form.buy.data:
			return redirect(url_for('product.buy', productid=product.id, distance=distance, quantity=quantity))

	return render_template('quotation.html', form=form, product=product)


@product_page.route('/product/<productid>/buy', methods=['GET', 'POST'])
@login_required
def buy(productid):
	product = Product.get(productid)
	distance = request.args.get('distance', type=float)
	quantity = request.args.get('quantity', type=int)

	quote = product.quote(distance, quantity)

	form = BuyProductForm()
	if form.validate_on_submit():
		client = current_user
		client.buy_product(
			product, quote,
			form.number.data, form.cvx.data, form.expiration_date.data,
			form.first_name.data, form.last_name.data, form.birthday.data)

		return render_template('bill.html', product=product, quote=quote)

	return render_template('buy.html', product=product, quote=quote, form=form)
