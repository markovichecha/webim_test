from flask import Flask, request, redirect, render_template
import credentials as c
import datetime
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'token' in request.cookies:
        token = request.cookies.get('token')
        r = requests.get(c.get_name(token)).json()['responce']
        name = r['first_name'] + " " + r['last_name']
        return render_template('list.html', name=name)
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return redirect(c.code_url())


@app.route('/authorize', methods=['GET'])
def authorize():
    if c.STATE == request.args.get('state'):
        token = requests.get(c.access_url(request.args.get('code'))).json()['access_token']
        return app.make_response(redirect('/')).set_cookie('token', value=token,
                                                           expires=datetime.datetime.now() + datetime.timedelta(days=1))
    else:
        return request.args.get('state')