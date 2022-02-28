from email import header
from flask import Flask, request
from pprint import pprint as pp
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Merge Logs APIs Working</h1>"

@app.route('/github_webhook', methods=['POST'])
def github_webhook():
    output = request.json
    action = output.get('action')
    repository = output['repository']['html_url']
    repository_name = output['repository']['name']
    owner = output['repository']['owner']['html_url']
    owner_name = output['repository']['owner']['login']
    base_branch = output['pull_request']['base']['label']
    base_branch_ref = output['pull_request']['base']['sha']
    head_branch = output['pull_request']['head']['label']
    sender = output['sender']['html_url']
    pp(output)
    base_branch_data = base_branch.split(":")
    status_json = requests.get(f"https://api.github.com/repos/{owner_name}/{repository_name}/commits/{base_branch_ref}/statuses", headers={"Accept": "application/vnd.github.v3+json"})
    pp(status_json.json())
    log = f"Action: {action} - Repository: {repository} - Owner: {owner} - Base_Branch: {base_branch} - Head_Branch: {head_branch} - Sender: {sender}"
    print(log)
    return "Done"

@app.route('/gitlab_webhook')
def gitlab_webhook():
    pass

if __name__ == '__main__':
    app.run(debug=True)