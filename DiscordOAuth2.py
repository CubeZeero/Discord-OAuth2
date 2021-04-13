from flask import Flask, request, render_template
import webbrowser
import requests
import json

app = Flask(__name__)

port = 5000
client_id = 'YOUR CLIENT_ID HERE'
client_secret = 'YOUR CLIENT_SECRET HERE'
callback_url = 'http://localhost:'+ str(port) +'/callback/'

login_url = 'https://discord.com/api/oauth2/authorize?response_type=code&client_id='+ client_id +'&scope=identify&redirect_uri='+ callback_url + '&prompt=consent'

webbrowser.open(login_url)

@app.route('/callback/')
def hello():
    authorization_code = request.args.get("code")

    request_postdata = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_url}
    accesstoken_request = requests.post('https://discord.com/api/oauth2/token', data=request_postdata)

    responce_json = accesstoken_request.json()

    access_token = responce_json['access_token']
    token_type = responce_json['token_type']
    expires_in = responce_json['expires_in']
    refresh_token = responce_json['refresh_token']
    scope = responce_json['scope']

    responce_txt = open('responce.txt', 'w')
    responce_txt.write('access_token: '+ access_token +'\ntoken_type: '+ token_type +'\nexpires_in: '+ str(expires_in) +'\nrefresh_token: '+ refresh_token +'\nscope: '+ scope)

    return render_template('complete_window.html', title='Complete')

if __name__ == "__main__":
    app.run(port=port)
