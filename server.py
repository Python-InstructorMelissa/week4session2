from flask import Flask, render_template, request, redirect, session
import os
from data.user import user
from data.food import food


app = Flask(__name__)
app.secret_key = os.environ['KEY']

@app.route('/')
def index():
    return render_template('index.html', users=user)

@app.route('/choseUser/', methods=['POST'])
def choseUser():
    print("the option chosen", request.form)
    session['firstName'] = request.form['firstName']
    return redirect('/viewUser/')

@app.route('/createDrink/', methods=['POST'])
def createDrink():
    session['drink'] = request.form['drink']
    return redirect('/drink/')

@app.route('/viewUser/')
def viewUser():
    return render_template('viewUser.html', user=user)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/foods/')
def meals():
    if 'firstName' not in session:
        return redirect('/')
    else:
        return render_template('food.html', foods=food)

@app.route('/drink/')
def drink():
    return render_template('drink.html')





if __name__=="__main__":
    app.run(debug=True)

