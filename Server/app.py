from flask import Flask, render_template, current_app, request, redirect
from pymongo.mongo_client import MongoClient

from dotenv import load_dotenv
import os

load_dotenv("../.env")

mongdb_pass = os.getenv("MONGODB_PASS")
mongodb_uname = os.getenv("MONGODB_USERNAME")
mongodb_cluster = os.getenv("MONGODB_CLUSTER")

mongo_uri = "mongodb+srv://"+ mongodb_uname + ":" + mongdb_pass + "@" + mongodb_cluster + ".mongodb.net/?retryWrites=true&w=majority"

app = Flask(__name__)

@app.route("/")
def index_page():
    return current_app.send_static_file('index.html')

@app.route("/about.html")
def about_page():
    return current_app.send_static_file('about.html')

@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        dbClient = MongoClient(mongo_uri)
        db = dbClient["budgetbitez"]
        recipeCollection = db["recipes"]
        budget = request.form["budget"]

        recipeResults = recipeCollection.find({"$expr": {"$lte": [budget, {"$sum": "ingredients.price"}]}}).limit(10).toList()

        return render_template("results.html", recipeResults, budget)

    else:
        return render_template("results.html")