from flask import Flask, render_template
from data.tunesData import theTunes
from data.squishyData import squish

app = Flask(__name__)

@app.route('/') # This is telling our application what the url is going to be 
def index(): # This is the function that will run when the above url is hit (or types it in)
    return render_template('index.html', squishies=squish, tunes=theTunes) # return and print to the screen render the html doc listed with the following data allowed squishies=squish the 1st squishies = what I will use on the html to reference the data which is the 2nd one
    # Anything that you want the html doc to have access to or to display needs to be listed in the () with the html docs name

@app.route('/table/')
def table():
    return render_template('table.html', squishies=squish, tunes=theTunes)



if __name__=="__main__":
    app.run(debug=True)

