from flask import Flask, request
from markupsafe import Markup, escape

app = Flask(__name__)


@app.route("/hosts")
def hosts():
    return """
        <html>
            <body>
                <h1>list existing hosts</h1>
            </body>
        </html>
        """


@app.route("/hosts/add")
def newhost():
    return """
        <html>
            <body>
                <h1>Add a new ssh host</h1>
            </body>
        </html>
        """


@app.route("/keys")
def keys():
    return """
        <html>
            <body>
                <h1>manage keys here</h1>
            </body>
        </html>
        """
