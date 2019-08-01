from flask import render_template, request, Blueprint
from flask_api import FlaskAPI


core = Blueprint('core', __name__)

@core.route('/', methods=['GET', 'POST'])
def my_index():
    # return render_template('index.html', token="Hello Flask+react")
    return {'hello': 'world'}