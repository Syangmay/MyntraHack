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

@app.route('/menjackets2')
def menjackets2():
    return render_template("menjackets2.html")

@app.route('/menjackets3')
def menjackets3():
    return render_template("menjackets3.html")

@app.route('/menjackets4')
def menjackets4():
    return render_template("menjackets4.html")

@app.route('/menjackets5')
def menjackets5():
    return render_template("menjackets5.html")

@app.route('/menjackets6')
def menjackets6():
    return render_template("menjackets6.html")

@app.route('/menjackets7')
def menjackets7():
    return render_template("menjackets7.html")

@app.route('/menjackets8')
def menjackets8():
    return render_template("menjackets8.html")

@app.route('/menjackets9')
def menjackets9():
    return render_template("menjackets9.html")

@app.route('/menjackets10')
def menjackets10():
    return render_template("menjackets10.html")

@app.route('/bodytype')
def bodytype():
    return render_template("bodytype.html")

@app.route('/end')
def end():
    return render_template("end.html")



@app.route('/menjeans')
def menjeans():
    return render_template("menjeans.html")

@app.route('/menjeans1')
def menjeans1():
    return render_template("menjeans1.html")

@app.route('/menjeans2')
def menjeans2():
    return render_template("menjeans2.html")

@app.route('/menjeans3')
def menjeans3():
    return render_template("menjeans3.html")

@app.route('/menjeans4')
def menjeans4():
    return render_template("menjeans4.html")

@app.route('/menjeans5')
def menjeans5():
    return render_template("menjeans5.html")

@app.route('/menjeans6')
def menjeans6():
    return render_template("menjeans6.html")






@app.route('/menshirt')
def menshirt():
    return render_template("menshirt.html")

@app.route('/menshirt1')
def menshirt1():
    return render_template("menshirt1.html")

@app.route('/menshirt2')
def menshirt2():
    return render_template("menshirt2.html")

@app.route('/menshirt3')
def menshirt3():
    return render_template("menshirt3.html")

@app.route('/menshirt4')
def menshirt4():
    return render_template("menshirt4.html")

@app.route('/menshirt5')
def menshirt5():
    return render_template("menshirt5.html")






@app.route('/mentshirt')
def mentshirt():
    return render_template("mentshirt.html")

@app.route('/women')
def women():
    return render_template("women.html")

@app.route('/womenjumpsuit')
def womenjumpsuit():
    return render_template("womenjumpsuit.html")

@app.route('/womenjeans')
def womenjeans():
    return render_template("womenjeans.html")

@app.route('/womenjumpsuit1')
def womenjumpsuit1():
    return render_template("womenjumpsuit1.html")

@app.route('/womenjumpsuit2')
def womenjumpsuit2():
    return render_template("womenjumpsuit2.html")

@app.route('/womenjumpsuit3')
def womenjumpsuit3():
    return render_template("womenjumpsuit3.html")

@app.route('/womenjumpsuit4')
def womenjumpsuit4():
    return render_template("womenjumpsuit4.html")

@app.route('/womenjumpsuit5')
def womenjumpsuit5():
    return render_template("womenjumpsuit5.html")

@app.route('/womenjumpsuit6')
def womenjumpsuit6():
    return render_template("womenjumpsuit6.html")

if __name__ == "__main__":
    app.run(debug=True)
