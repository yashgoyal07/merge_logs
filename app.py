import logging
from flask import Flask, request
from pprint import pprint as pp
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Check Logs APIs Working</h1>"

@app.route('/github_webhook', methods=['POST'])
def github_webhook():
    output = request.json
    action = output.get('action')
    repository = output['repository']['html_url']
    owner = output['repository']['owner']['html_url']
    base_branch = output['pull_request']['base']['label']
    head_branch = output['pull_request']['head']['label']
    head_url = output['pull_request']['url']
    sender = output['sender']['html_url']
    pp(output)
    status_json = requests.get(head_url, headers={"Accept": "application/vnd.github.v3+json"})
    status = status_json.json()
    log = f"Action: {action} - Repository: {repository} - Owner: {owner} - Base_Branch: {base_branch} - Head_Branch: {head_branch} - Sender: {sender} - Merged: {status['merged']} - Mergeable: {status['mergeable']} - Mergeable State: {status['mergeable_state']}"
    print(log)
    return "Done"

@app.route('/workflow_run', methods=['POST'])
def workflow_run():
    output = request.json
    action = output.get('action')
    id = output['workflow_run']['id']
    status = output['workflow_run']['status']
    conclusion = output['workflow_run']['conclusion']
    log = f"Workflow Run id: {id} {action} with current status: {status} and conclusion: {conclusion}"
    print(log)
    return "Done"

@app.route('/workflow_job', methods=['POST'])
def workflow_job():
    output = request.json
    action = output.get('action')
    id = output['workflow_job']['id']
    status = output['workflow_job']['status']
    conclusion = output['workflow_job']['conclusion']
    steps = output['workflow_job']['steps']
    log = f"Workflow Job id: {id} {action} with current status: {status} and conclusion: {conclusion} with steps below:"
    print(log)
    for step in steps:
        print(f"Name: {step['name']} - Status: {step['status']} - Conclusion: {step['conclusion']}")
    return "Done"

@app.route('/pull_request', methods=['POST'])
def pull_request():
    output = request.json
    action = output.get('action')
    base_branch = output['pull_request']['base']['label']
    head_branch = output['pull_request']['head']['label']
    log = f"Pull Request {action} to merge {head_branch} to {base_branch}"
    print(log)
    return "Done"

@app.route('/check_suite', methods=['POST'])
def check_suite():
    output = request.json
    action = output.get('action')
    id = output['check_suite']['id']
    status = output['check_suite']['status']
    conclusion = output['check_suite']['conclusion']
    log = f"Check Suite id: {id} {action} with current status: {status} and conclusion: {conclusion}"
    print(log)
    return "Done"

@app.route('/check_run', methods=['POST'])
def check_run():
    output = request.json
    action = output.get('action')
    id = output['check_run']['id']
    status = output['check_run']['status']
    conclusion = output['check_run']['conclusion']
    log = f"Check Run id: {id} {action} with current status: {status} and conclusion: {conclusion}"
    print(log)
    return "Done"



if __name__ == '__main__':
    app.run(debug=True)