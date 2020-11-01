from flask import Flask, request, render_template, render_template_string

import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/begin')
def begin():
    return render_template("page1.html")

@app.route('/gender')
def gender():
    return render_template("gender.html")

if __name__ == "__main__":
    app.run(debug=True)
