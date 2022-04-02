
from utils import app

@app.route("/posts")
def posts():
    pass

@app.route("/posts/submit", methods=['GET','POST'])
def submit():
    pass
        