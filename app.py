from flask import Flask, render_template, request, jsonify
import pandas as pd
from model.recommender import Recommender

app = Flask(__name__)

recommender = Recommender()

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get('q', '').lower()
    if query:
        matching_animes = recommender.data[recommender.data['Name'].str.contains(query, case=False)]
        titles = matching_animes[['anime_id', 'Name']].to_dict(orient='records')
        return jsonify(titles)
    return jsonify([])

@app.route("/anime/<int:anime_id>", methods=["GET"])
def get_anime_details(anime_id):
    anime = recommender.data[recommender.data['anime_id'] == anime_id].to_dict(orient='records')[0]
    recommendations = recommender.recommend(id=anime_id, count=12).to_dict(orient='records')
    return jsonify({"anime": anime, "recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
