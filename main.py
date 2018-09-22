from flask import Flask, request, redirect, render_template
import credentials as c
import datetime
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'token' in request.cookies:
        token = request.cookies.get('token')
        r = requests.get(c.get_name(token)).json()['response'][0]
        name = r['first_name'] + " " + r['last_name']
        friends = requests.get(c.get_friends(token)).json()['response']['items']
        return render_template('list.html', name=name, friends=friends)
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return redirect(c.code_url())
    else:
        return redirect("/")


@app.route('/authorize', methods=['GET'])
def authorize():
    if request.args.get("state") == c.STATE:
        token = requests.get(c.access_url(request.args.get('code'))).json()['access_token']
        responce = app.make_response(redirect('/'))
        responce.set_cookie('token', value=token, expires=datetime.datetime.now() + datetime.timedelta(days=1))
        return responce
    else:
        return redirect("/")