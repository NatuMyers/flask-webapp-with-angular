__author__ = 'danielqueiroz'

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound




#PAGES ---
# replace "deceptron" with the name of this file

# deceptron page blueprint
deceptron = Blueprint('deceptron', __name__, template_folder='templates')
# what the user needs to enter as an url to to get to this file
@deceptron.route('/deceptron', defaults={'page': 'index'})
# end page


#to work with pages and get suburls
@deceptron.route('/deceptron/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)




