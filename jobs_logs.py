import requests

owner = "geekcomputers"
repo = "Python"
run_id = "1353863430"

jobs_url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/jobs"

response = requests.get(jobs_url, headers={"Accept": "application/vnd.github.v3+json"})

response_json = response.json()

total_jobs = response_json['total_count']

bold_start = '\033[1m'
bold_end = '\033[0m'

print(f'{bold_start}Total Jobs{bold_end}: {total_jobs}\n')

jobs = response_json['jobs']

for job in jobs:
    print(f"{bold_start}Logs of job id: {job['id']} given below:{bold_end}\n")
    for step in job['steps']:
        print(f"--> {bold_start}Name{bold_end}: {step['name']} - {bold_start}Status{bold_end}: {step['status']} - {bold_start}Conclusion{bold_end}: {step['conclusion']}\n")

    check_run_url = job['check_run_url']

    annotation_url = check_run_url + '/annotations'

    annotations = requests.get(annotation_url, headers={"Accept": "application/vnd.github.v3+json"})

    annotations_json = annotations.json()

    print(f"{bold_start}-- > Logs of annotations for this job given below:{bold_end}\n")
    for annotation in annotations_json:
        print(f"   --> {bold_start}Level{bold_end}: {annotation['annotation_level']} - {bold_start}Title{bold_end}: {annotation['title']} - {bold_start}Message{bold_end}: {annotation['message']}\n")
