from flask import request
from utils import app
from posts import controller

from flask_sqlalchemy import SQLAlchemy

POSTGRESQL_URI = "postgres://qqlyispm:oc8UNA3oxNUGg71TNNEV4WpyxJcO738c@john.db.elephantsql.com/qqlyispm"
app.config['SQLALCHEMY_DATABSE_URI'] = POSTGRESQL_URI

db = SQLAlchemy(app)

@app.route("/")
def posts():
    return "hello World !!"

@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        message = request.form['message']
        lat = request.form['lat']
        lon = request.form['lon']
        post = controller.Posts(message,lat,lon)
        db.session.add(post)
        db.session.commit()
        