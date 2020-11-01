from flask import Flask, request, render_template, render_template_string

import pandas as pd

mjackets = {}
mjeans = {}
mshirts = {}
mtshirts = {}

jackets = []
jacketcount = [0] * 15


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



@app.route('/menjackets', methods=['get','post'])
def menjackets():
    return render_template("menjackets.html")

@app.route('/menjackets2', methods=['get','post'])
def menjackets2():
    return render_template("menjackets2.html")

@app.route('/menjackets3', methods=['get','post'])
def menjackets3():
    if request.method == 'POST':
        weather = request.form.get('gender')

        if weather == "yes" :
            attributes = ["Quilted" , "Bomber", "Puffer" , "Padded" , "Leather", "Full Sleeve"]
            for i in range(len(attributes)):
                if attributes[i] not in jackets:
                    jackets.append(attributes[i])
                jacketcount[jackets.index(attributes[i])] += 1
        print("weather:")
        print(jackets)
        print(jacketcount)

    return render_template("menjackets3.html")

@app.route('/menjackets4', methods=['get','post'])
def menjackets4():
    if request.method == 'POST':
        biking = request.form.get('biking')
        attributes = ["Bomber", "Leather"]

        if biking == "often" :
            for i in range(len(attributes)):
                if attributes[i] not in jackets:
                    jackets.append(attributes[i])
                jacketcount[jackets.index(attributes[i])] += 1
        elif biking=="sometimes":
            for i in range(len(attributes)):
                if attributes[i] not in jackets:
                    jackets.append(attributes[i])
                jacketcount[jackets.index(attributes[i])] += 0.5
    print("biking:")
    print(jackets)
    print(jacketcount)
    return render_template("menjackets4.html")

@app.route('/menjackets5', methods=['get','post'])
def menjackets5():
    if request.method == 'POST':
        sports = request.form.get('sports')

        if sports == "yes" :
            attributes = ["Sporty"]
            for i in range(len(attributes)):
                if attributes[i] not in jackets:
                    jackets.append(attributes[i])
                jacketcount[jackets.index(attributes[i])] += 1

        print("sports:")
        print(jackets)
        print(jacketcount)

    return render_template("menjackets5.html")

@app.route('/menjackets6', methods=['get','post'])
def menjackets6():

    if request.method == 'POST':
        party = request.form.get('party')
        attributes = ["Tailored" , "Bomber", "Denim", "Leather"]

        if party == "often" :
            for i in range(len(attributes)):
                if attributes[i] not in jackets:
                    jackets.append(attributes[i])
                jacketcount[jackets.index(attributes[i])] += 1
        elif party=="sometimes":
            for i in range(len(attributes)):
                if attributes[i] not in jackets:
                    jackets.append(attributes[i])
                jacketcount[jackets.index(attributes[i])] += 0.5
        elif party=="rarely":
            for i in range(len(attributes)):
                if attributes[i] not in jackets:
                    jackets.append(attributes[i])
                jacketcount[jackets.index(attributes[i])] += 0.25

    print("party:")
    print(jackets)
    print(jacketcount)
    return render_template("menjackets6.html")

@app.route('/menjackets7')
def menjackets7():
    if request.method == 'POST':
        formal = request.form.get('formal')

        if formal == "yes" :
            attributes = ["Puffer", "Padded", "Bomber"]
            for i in range(len(attributes)):
                if attributes[i] not in jackets:
                    jackets.append(attributes[i])
                jacketcount[jackets.index(attributes[i])] += 1
        print("daily:")
        print(jackets)
        print(jacketcount)

    return render_template("menjackets7.html")

@app.route('/menjackets8')
def menjackets8():
    attr = []
    count = []
    return render_template("menjackets8.html")

@app.route('/menjackets9')
def menjackets9():
    attr = []
    count = []
    return render_template("menjackets9.html")

@app.route('/menjackets10')
def menjackets10():
    if request.method == 'POST':
        closure = request.form.get('prefer')

        if closure not in jackets:
            jackets.append(closure)
        jacketcount[jackets.index(closure)] += 1

        print("closure:")
        print(jackets)
        print(jacketcount)
    return render_template("menjackets10.html")

@app.route('/bodytype')
def bodytype():
    attr = []
    count = []
    return render_template("bodytype.html")

@app.route('/end')
def end():
    attr = []
    count = []
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

@app.route('/mentshirt')
def mentshirt():
    return render_template("mentshirt.html")

@app.route('/mentshirt1')
def mentshirt1():
    return render_template("mentshirt1.html")

@app.route('/mentshirt2')
def mentshirt2():
    return render_template("mentshirt2.html")

@app.route('/mentshirt3')
def mentshirt3():
    return render_template("mentshirt3.html")

@app.route('/mentshirt4')
def mentshirt4():
    return render_template("mentshirt4.html")

@app.route('/mentshirt5')
def mentshirt5():
    return render_template("mentshirt5.html")

@app.route('/mentshirt6')
def mentshirt6():
    return render_template("mentshirt6.html")

if __name__ == "__main__":
    app.run(debug=True)
