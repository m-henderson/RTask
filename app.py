from functools import wraps
import json
import config
from os import environ as environ
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask import request
from flask import flash
from authlib.flask.client import OAuth
from six.moves.urllib.parse import urlencode
from models.ticket import Ticket
from forms.ticket_form import TicketForm
from flask import g
from models.ticket import db_session

app = Flask(__name__)
app.secret_key = 'SlumDog'
oauth = OAuth(app)

# move to config file
auth0 = oauth.register(
    'auth0',
    client_id=config.clientId,
    client_secret= config.secret,
    api_base_url='https://rtask.auth0.com',
    access_token_url='https://rtask.auth0.com/oauth/token',
    authorize_url='https://rtask.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)

@app.route('/')
def hello():
    name = 'michael'
    return render_template('home.html', name=name)

@app.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }

    return redirect('/dashboard')

@app.route('/login')
def login():
    return auth0.authorize_redirect(redirect_uri='http://localhost:5000/callback')

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if 'profile' not in session:
      # Redirect to Login page here
      return redirect('/')
    return f(*args, **kwargs)

  return decorated

@app.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('/dashboard/index.html',
                           userinfo=session['profile'],
                           userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))

@app.route('/logout')
def logout():
    # Clear session stored data
    db_session.clear()
    # Redirect user to logout endpoint
    params = {'returnTo': url_for('home', _external=True), 'client_id': 'Zt9tC9dhE4oGIqS5JDyUbbVg6ykZ0zVY'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

@app.route('/dashboard/tickets/new', methods=['GET', 'POST'])
def ticket():

    ticket = Ticket()
    success = False
    form = TicketForm(request.form, obj=ticket)

    if request.method == 'GET':
        form = TicketForm(obj=ticket)
        return render_template('/dashboard/tickets/new.html', form=form, success=success)
    
    ticket.title = request.form['title']
    ticket.description = request.form['description']

    g.db.add(ticket)
    g.db.commit()
    success = True

    flash('ticket created successfully!')
    return redirect(url_for('ticket_list'))

@app.route('/dashboard/tickets', methods=['GET'])
def ticket_list():
    # get list of tickets
    tickets = getTickets()

    return render_template('/dashboard/tickets/index.html', tickets=tickets)

@app.route('/dashboard/tickets/<int:ticket_id>', methods=['GET'])  
def get_ticket(ticket_id):
    ticket = g.db.query(Ticket).get(ticket_id)
    return render_template('/dashboard/tickets/view.html', ticket=ticket)

@app.before_request
def before_req():
    g.db = db_session()

@app.after_request
def after_req(resp):
    try:
        g.db.close()
    except Exception:
        pass
    return resp

def getTickets():
    tickets = g.db.query(Ticket).all()
    for ticket in tickets:
        print(ticket.description)
    return tickets

    
if __name__ == '__main__':
    db.create_all()

    app.run(debug=True)