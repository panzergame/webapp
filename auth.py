from flask import Blueprint, render_template
from forms.register_client import RegisterClientForm

auth_page = Blueprint('auth', __name__)

@auth_page.route('/client/register', methods=['GET', 'POST'])
def register_client():
    form = RegisterClientForm()
    if form.validate_on_submit():
        return 

    return render_template('register_client.html', form=form)
