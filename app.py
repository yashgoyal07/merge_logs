from flask import Flask, request
from pprint import pprint as pp

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Merge Logs APIs Working</h1>"

@app.route('/github_webhook', methods=['POST'])
def github_webhook():
    output = request.json()
    pp(output)
    return "Done"
    
@app.route('/gitlab_webhook')
def gitlab_webhook():
    pass

if __name__ == '__main__':
    app.run(debug=True)