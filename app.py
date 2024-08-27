from flask import Flask, render_template, request, jsonify
import pandas as pd
from model.recommender import Recommender

app = Flask(__name__)

recommender = Recommender()

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")
    pass

def before_request():
    app.jinja_env.cache = {}

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.before_request(before_request)
    app.run(debug=True)
    # print(recommender.recommend(title = "trigun"))
