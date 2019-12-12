from flask import Blueprint, jsonify, render_template, request
from requests_oauthlib import OAuth2Session
import requests

mod = Blueprint('fork_repo', __name__)

@mod.route('/test', methods=['GET'])
def test_route():
   return {'result': 'Hitting the fork_repo blueprint'}

@mod.route('/login')
def login():
   client_id = 'a199df7116a41d717d94'
   authorization_base_url = 'https://github.com/login/oauth/authorize'
   github = OAuth2Session(client_id)
   authorization_url, state = github.authorization_url(authorization_base_url)
   return {'authorizationLink': authorization_url}

@mod.route('/login/githubRedirect')
def auth():
   client_id = 'client id from github'
   client_secret = 'client secret from github'
   redirect_response = request.url
   github = OAuth2Session(client_id)
   token_url = 'https://github.com/login/oauth/access_token'
   github.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)
   r = github.post('https://api.github.com/repos/marblexu/PythonPlantsVsZombies/forks')
   return r

@mod.route('/fork-repo/<string:user_name>/<string:repo_name>')
def fork(user_name, repo_name):
   client_id = 'client id from github'
   github = OAuth2Session(client_id)
   r = github.get('https://api.github.com/repos/'+user_name+ '/' + repo_name + '/forks')
 
