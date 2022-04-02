from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = "developement"
app.config['FLASK_APP'] = "run.py"

from posts import routs
from weather import models