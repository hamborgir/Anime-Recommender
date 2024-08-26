from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<p> TES </p>"


with app.test_request_context():
    print(url_for("static", filename = "style.css"))