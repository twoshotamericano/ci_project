"""Minimal Flask Application 2"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Default Path
    """

    return "<p>Hello, World!</p>"
