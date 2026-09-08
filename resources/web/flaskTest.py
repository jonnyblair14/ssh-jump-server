import hostops
from flask import Flask, redirect, render_template, request, url_for
from markupsafe import Markup, escape

app = Flask(__name__)


@app.route("/hosts")
def hosts():
    return "<h1>list existing hosts</h1>"


@app.route("/hosts/add", methods=["GET", "POST"])
def newhostpage():
    if request.method == "POST":
        name = request.form["friendlyName"]
        hostname = request.form["hostName"]
        username = request.form["userName"]
        port = request.form["port"]
        idFile = request.form["identityFile"]

        hostops.newhost(
            hostname=hostname, name=name, user=username, port=port, idFile=idFile
        )
        return redirect(url_for("hosts"))

    return render_template("add-host.html")


@app.route("/keys")
def keys():
    return "<h1>manage keys here</h1>"
