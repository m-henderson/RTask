from flask import Flask, escape, request, render_template, Response
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# Our mock database
users = {'mvhenderson.4@gmail.com': {'password': 'secret'}}

@app.route('/')
def hello():
    name = 'michael'
    return render_template('home.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template('login.html')

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))
    
    return 'Bad login'
    

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)