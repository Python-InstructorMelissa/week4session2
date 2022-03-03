from flask import Flask, render_template, session, request, redirect
from env import KEY

app = Flask(__name__)
# app.secret_key = 'Dont touch my secret'
app.secret_key = KEY

theMovies = []
print(theMovies)

# Landing page
@app.route('/')
def index():
    return render_template('index.html')


# Hidden Route
@app.route('/createUser/', methods=['post'])
def createUser():
    print('Form submition was good')
    print('Here is the data', request.form['name'])
    session['name'] = request.form['name']
    return redirect('/movies/')

@app.route('/movies/')
def movies():
    # session['title']
    # if not session['title']:  # this is how we ended class
    if 'title' not in session: # this is what it should have been
        return render_template('movies.html')
    else:
        data = session['title']
        theMovies.append(data)
        return render_template('movies.html', movieList=theMovies)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

# This is what will clear just the movie list
@app.route('/reset/')
def reset():
    session.pop('title')
    return redirect('/movies/')

@app.route('/createMovie/', methods=['POST'])
def createMovie():
    print('Movie data', request.form['title'])
    session['title'] = request.form['title']
    return redirect('/movies/')


if __name__=="__main__":
    app.run(debug=True)

