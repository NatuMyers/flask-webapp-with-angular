# -*- coding: utf-8 -*-
import os
DIR = os.path.dirname(os.path.abspath(__file__))

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from lib.translate import translate



from flask import  Blueprint, abort, make_response
from jinja2 import TemplateNotFound
deceptron = Blueprint('deceptron',__name__)


@deceptron.route('/deceptron', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        text = data[u'text']
        result = translate(text)
        return result
    else:
        return make_response(open(os.path.join(DIR, 'deceptron.html')).read())



