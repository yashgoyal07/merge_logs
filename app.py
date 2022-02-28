from flask import Flask, request
from pprint import pprint as pp

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Merge Logs APIs Working</h1>"

@app.route('/github_webhook', methods=['POST'])
def github_webhook():
    output = request.json
    action = output.get('action')
    repository = output['repository']['html_url']
    owner = output['repository']['owner']['html_url']
    base_branch = output['pull_request']['base']['label']
    head_branch = output['pull_request']['head']['label']
    sender = output['sender']['html_url']
    pp(output)
    log = f"Action: {action} - Repository: {repository} - Owner: {owner} - Base_Branch: {base_branch} - Head_Branch: {head_branch} - Sender: {sender}"
    print(log)
    return "Done"

@app.route('/gitlab_webhook')
def gitlab_webhook():
    pass

if __name__ == '__main__':
    app.run(debug=True)