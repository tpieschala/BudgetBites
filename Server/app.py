from flask import Flask, render_template, current_app

app = Flask(__name__)

@app.route("/")
def index_page():
    return current_app.send_static_file('index.html')

@app.route("/about.html")
def about_page():
    return current_app.send_static_file('about.html')
