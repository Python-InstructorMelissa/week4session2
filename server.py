from flask import Flask, render_template, request, redirect, session
from env import KEY
from data.data import *

app = Flask(__name__)
app.secret_key = KEY

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/addPark', methods=['POST'])
def createPark():
    print("Got your form submission")
    print(request.form)
    session['park'] = request.form['parkName']
    return redirect('/parks')

@app.route('/parks')
def parks():
    return render_template('parks.html', animals=animals)

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')







if __name__=="__main__":
    app.run(debug=True)

