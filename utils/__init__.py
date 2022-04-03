from flask import Flask,render_template

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = "developement"
app.config['FLASK_APP'] = "run.py"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:killermb@localhost/flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def home():
    return render_template('main.html')

import posts
import weather