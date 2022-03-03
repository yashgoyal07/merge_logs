import requests

owner = "geekcomputers"
repo = "Python"
run_id = "1353863430"

jobs_url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/jobs"

response = requests.get(jobs_url, headers={"Accept": "application/vnd.github.v3+json"})

response_json = response.json()

total_jobs = response_json['total_count']

print(f'\033[1mTotal Jobs\033[0m: {total_jobs}\n')

jobs = response_json['jobs']

for job in jobs:
    print(f"\033[1mLogs of job id: {job['id']} given below\033[0m\n")
    for step in job['steps']:
        print(f"--> \033[1mName\033[0m: {step['name']} - \033[1mStatus\033[0m: {step['status']} - \033[1mConclusion\033[0m: {step['conclusion']}\n")
