from flask import Flask
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='',
    client_secret='',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs=('scope': 'openid profile email'),
)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.twitter.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = oauth.twitter.authorize_access_token()
    resp = oauth.twitter.get('userinfo')
    resp.raise_for_status()
    userinfo = resp.json()
    # do something with the token and profile
    return redirect('/')