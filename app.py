from flask import Flask, url_for, redirect, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'random secret'

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='1058292961152-516pk7ud7alevj9kkqev1s5oiumk5oib.apps.googleusercontent.com',
    client_secret='i5-6yk-wm-yl5X63X2c9Tue8',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)

@app.route("/")
def hello():
    email = dict(session).get('email', None)
    return "Hello {email}!"

@app.route('/login')
def login():
    google =oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    resp.raise_for_status()
    userinfo = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    return redirect('/')