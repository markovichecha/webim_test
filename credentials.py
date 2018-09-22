from urllib.parse import urlencode

CLIENT_ID = "6699809"
CLIENT_SECRET= "pQJaPrdCx3qy66grUqhc"
REDIRECT_URI = "https://webim-test.herokuapp.com/authorize"
RESPONSE_TYPE = "code"
DISPLAY = "page"
SCOPE = "friends, users"
V = "5.85"
FIELDS = "photo, name"
ORDER = "random"
STATE = 389730183
COUNT = "5"

PARAMETERS_CODE = {'client_id': CLIENT_ID,
                   'response_type': RESPONSE_TYPE, 'display': DISPLAY, 'scope': SCOPE, 'v': V, 'state': STATE}

PARAMETERS_AUTH = {'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET, 'v': V}

PARAMETERS_FRIENDS = {'fields': FIELDS, 'order': ORDER, 'count': COUNT, 'v': V}

REQUEST_URL = "https://api.vk.com/method/"


def code_url():
    return "https://oauth.vk.com/authorize?redirect_uri=" + REDIRECT_URI + "&" + urlencode(PARAMETERS_CODE)

def access_url(code):
    return "https://oauth.vk.com/access_token?redirect_uri=" + REDIRECT_URI + "&" + urlencode(PARAMETERS_AUTH) + "&code=" + code

def get_name(token):
    return REQUEST_URL + "users.get?access_token=" + token + "&v=" + V

def get_friends(token):
    return REQUEST_URL + "friends.get?access_token=" + token + "&" + urlencode(PARAMETERS_FRIENDS)
