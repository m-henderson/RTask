from flask import Flask, escape, request, render_template, Response

app = Flask(__name__)

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

