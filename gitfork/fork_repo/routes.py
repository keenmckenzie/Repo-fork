from flask import Blueprint, jsonify, render_template, request
from requests_oauthlib import OAuth2Session
import requests

mod = Blueprint('fork_repo', __name__)

@mod.route('/test', methods=['GET'])
def test_route():
   return {'result': 'Hitting the fork_repo blueprint'}

@mod.route('/login')
def login():
   client_id = 'app client id from github'
   authorization_base_url = 'https://github.com/login/oauth/authorize'
   github = OAuth2Session(client_id)
   authorization_url, state = github.authorization_url(authorization_base_url)
   return {'authorizationLink': authorization_url}

@mod.route('/login/githubRedirect')
def auth():
   client_id = 'app client id from github'
   client_secret = 'app client secret from github'
   redirect_response = request.url
   github = OAuth2Session(client_id)
   token_url = 'https://github.com/login/oauth/access_token'
   github.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)
   r = github.get('https://api.github.com/user')
   return r.content
 
