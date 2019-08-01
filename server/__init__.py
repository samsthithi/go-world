import os
from flask import Flask, render_template
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

from server.core.views import core

app.register_blueprint(core)