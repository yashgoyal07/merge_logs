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
    base_branch_ref = output['pull_request']['head']['title']
    head_branch = output['pull_request']['head']['label']
    head_url = output['pull_request']['url']
    sender = output['sender']['html_url']
    # pp(output)
    status_json = requests.get(head_url, headers={"Accept": "application/vnd.github.v3+json"})
    status = status_json.json()
    log = f"Action: {action} - Repository: {repository} - Owner: {owner} - Base_Branch: {base_branch} - Head_Branch: {head_branch} - Sender: {sender} - Merged: {status['merged']} - Mergeable: {status['mergeable']} - Mergeable State: {status['mergeable_state']}"
    print(log)
    return "Done"

@app.route('/gitlab_webhook')
def gitlab_webhook():
    pass

if __name__ == '__main__':
    app.run(debug=True)