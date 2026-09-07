from flask import Flask, request
from markupsafe import Markup, escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/list")
def hello():
    return "<p>list existing hosts</p>"


@app.route("/new-host")
def newhost():
    return "<h1>Add a new ssh host</h1>"
