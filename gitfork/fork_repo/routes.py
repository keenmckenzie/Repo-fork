from flask import Blueprint, jsonify, render_template
import requests

mod = Blueprint('fork_repo', __name__)

@mod.route('/test', methods=['GET'])
def test_route():
   return {'result': 'Hitting the fork_repo blueprint'}

@mod.route('/callback', methods=['GET'])
def oauth_callback():
   return {'result': 'Callback from oauth'}

@mod.route('/user_repos/<username>', methods=['GET'])
def get_repos(username):
   endpoint_url = 'https://api.github.com/users'
   url = endpoint_url + '/' + username + '/repos'
   repos = {}
   r = requests.get(url, params= {'u':'keenmckenzie:a1e9f9793dc0a08ddf426e546a168068b031ee5c'})
   response_json = r.json()
   for repo in response_json:
     name = repo['name']
     git_url = repo['git_url']
     repos[name] = git_url
   return jsonify({'repos': repos})

@mod.route('/fork_repo/<account>/<repo>', methods=['GET'])
def fork_repo(account, repo):
   endpoint_url = 'https://api.github.com/repos/'+account+ '/' + repo + '/forks'
   result = {}
   r = requests.post(endpoint_url, auth = ('keenmckenzie', 'a1e9f9793dc0a08ddf426e546a168068b031ee5c'))
   response_json = r.json()
   result['success'] = 'true'
   result['name'] = response_json['name']
   result['url'] = response_json['clone_url']
   return jsonify({'repo': result})

@mod.route('/test_template', methods=['GET'])
def test_template():
   return render_template('home.html')
