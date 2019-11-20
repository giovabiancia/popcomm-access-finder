from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for,
    render_template)

from popcomm.blueprints.contact.forms import ContactForm

contact = Blueprint('contact', __name__, template_folder='templates')


@contact.route('/')
def index():

    return render_template('popcomm/index.html')
