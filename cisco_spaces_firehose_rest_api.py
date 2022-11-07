import json
import requests
from os import environ

if 'TOKEN' in environ:
    token = environ['TOKEN']
    print(f"Got token {token}")
    headers = {'X-API-Key': token}
    r = requests.get('https://partners.dnaspaces.io/api/partners/v1/firehose/events', stream=True, headers=headers)
    if r.status_code == 200:
        print(f"Got status code {r.status_code}")
        for line in r.iter_lines():
            data = json.loads(line)
            print(data)
    else:
        print("Unable to connect to partners.dnaspaces.io. Status code", r.status_code)
else:
    print("Please set environment variable TOKEN before running.")