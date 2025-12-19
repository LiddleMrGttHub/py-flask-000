from flask import Flask, render_template

flask_app = Flask(__name__)

@flask_app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
