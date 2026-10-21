from flask import Flask
import datetime as dt
import mymodels

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>Hello, World! <b>{str(dt.datetime.now())}</b></p>"

@app.route("/query/<q>")
def ddg_query(q):
    return mymodels.ddg(q)

@app.route("/soma/<a>/<b>")
def soma(a, b):
    return str(mymodels.soma(a, b))

@app.route("/core")
def core():
    return "Vai Corinthans!!"