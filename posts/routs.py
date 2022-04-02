
from utils import app

@app.route("/")
def posts():
    return "help"
@app.route("/submit", methods=['GET','POST'])
def submit():
    pass
        