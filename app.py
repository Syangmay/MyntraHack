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

@app.route('/men')
def men():
    return render_template("men.html")

@app.route('/menjackets')
def menjackets():
    return render_template("menjackets.html")

@app.route('/menjeans')
def menjeans():
    return render_template("menjeans.html")

@app.route('/menshirt')
def menshirt():
    return render_template("menshirt.html")

@app.route('/mentshirt')
def mentshirt():
    return render_template("mentshirt.html")

@app.route('/women')
def women():
    return render_template("women.html")

if __name__ == "__main__":
    app.run(debug=True)
