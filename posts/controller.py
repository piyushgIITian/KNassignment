from utils import app
from flask_sqlalchemy import SQLAlchemy

POSTGRESQL_URI = "postgres://qqlyispm:oc8UNA3oxNUGg71TNNEV4WpyxJcO738c@john.db.elephantsql.com/qqlyispm"
app.config['SQLALCHEMY_DATABSE_URI'] = POSTGRESQL_URI

db = SQLAlchemy(app)

class Posts(db.model):
    __tablename__ = 'posts'
    message = db.Column(db.String(40),primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __init__(self,message,lat,lon):
        self.message = message
        self.lat = lat
        self.lon = lon