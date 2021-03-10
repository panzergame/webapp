from flask import Flask, render_template
from forms import register_client
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/client/register', methods=['GET', 'POST'])
def register_client_user():
    form = register_client.RegisterClientForm()
    if form.validate_on_submit():
        return "enregistré"
    return render_template('register_client.html', form=form)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
