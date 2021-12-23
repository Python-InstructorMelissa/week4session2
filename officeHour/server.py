from flask import Flask, render_template
from data.user import user
from data.tvShow import tvshow
from data.food import food
from data.sleep import sleep

app = Flask(__name__)

data = 1

@app.route('/')
def index():
    return render_template('index.html', user=user[data])

@app.route('/enter/')
def hall():
    return render_template('enter.html', user=user[data])

@app.route('/exit/')
def exit():
    return render_template('exit.html', user=user[data])

@app.route('/livingroom/')
def living():
    return render_template('living.html', user=user[data])

@app.route('/tv/')
def tv():
    return render_template('tv.html', user=user[data], tvshow=tvshow[data])

@app.route('/kitchen/')
def kitchen():
    return render_template('kitchen.html', user=user[data])

@app.route('/cook/')
def cook():
    return render_template('cook.html', user=user[data], food=food[data])

@app.route('/hallway/')
def hallway():
    return render_template('hall.html', user=user[data])

@app.route('/bedroom/')
def bedroom():
    return render_template('bedroom.html', user=user[data])

@app.route('/sleep/')
def nap():
    return render_template('sleep.html', sleep=sleep[data])

@app.route('/garage/')
def garage():
    return render_template('garage.html', user=user[data])

@app.route('/about/')
def about():
    return render_template('about.html', users=user, tvshow=tvshow, foods=food, sleeps=sleep)

@app.route('/user/<int:user_id>/view/')
def viewUser(user_id):
    return render_template('viewUser.html', user=user[user_id-1])

if __name__=="__main__":
    app.run(debug=True)

