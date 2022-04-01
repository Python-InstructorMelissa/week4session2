from flask import Flask, render_template, redirect, session, request # render_template displays html files, redirect will change the route, session is to put things in session, request is to handle for input
from env import KEY

app = Flask(__name__)
# app.secret_key = "Melissa's super secret key"
app.secret_key = KEY

thePets = []

# Landing page -  this should be seen in the address bar of the browser
@app.route('/')
def index():
    return render_template('index.html')


# Hidden route - You should never see this route in the address bar of the browser unless there is an error
@app.route('/createUser/', methods=['POST'])
def createUser():
    session['user'] = request.form['user']
    # request.form['user] is coming directly from our html page and we are saying we want it to be = to session['user'] thus putting that name into session
    return redirect('/pets/')

@app.route('/pets/')
def pets():
    # lines 26-27 are checking to make sure that a user is logged in
    if 'user' not in session:
        print("silly person your not logged in")
        return redirect('/')
    # lines 29-30 are checking to see if we have added any pets yet if we haven't (as in this is true) just render the html 
    if 'petName' not in session:
        print('your logged in but no pets are in the list')
        return render_template('pets.html')
    # The rest of this function assumes we have added pets and then gives us a way to display them
    else:
        data = session['petName']
        thePets.append(data)
        return render_template('pets.html', petList = thePets)
        # petList is what we need to use on the html to call the list   thePets is the list (aka data)

@app.route('/createPet/', methods=['POST'])
def createPet():
    session['petName'] = request.form['petName']
    return redirect('/pets/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

# This is what will clear just the movie list
@app.route('/reset/')
def reset():
    session.pop('petName')
    return redirect('/pets/')

if __name__=="__main__":
    app.run(debug=True)

