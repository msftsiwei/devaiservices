import sys
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    message = "Flask running with Meinheld and Gunicorn on Python {major}.{minor}".format(major=sys.version_info.major, minor=sys.version_info.minor)
    return message
