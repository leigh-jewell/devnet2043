import json
import requests
from datetime import datetime
from os import environ

if 'TOKEN' in environ:
    token = environ['TOKEN']
    print(f"Got token {token}")
    headers = {'X-API-Key': token}
    time_now = datetime.now()
    timestamp_now = time_now.timestamp() * 1000
    params = {'from_timestamp': timestamp_now}
    r = requests.get('https://partners.dnaspaces.io/api/partners/v1/firehose/events', stream=True, headers=headers,
                     params=params)
    before_timestamp = 0
    after_timestamp = 0
    total_events = 0
    if r.status_code == 200:
        print(f"Got status code {r.status_code}")
        with open('data.json', 'w') as f:
            for line in r.iter_lines():
                # filter out keep-alive new lines
                total_events += 1
                if line:
                    data = json.loads(line)
                    print(data)
                    record_timestamp = datetime.fromtimestamp(data['recordTimestamp']/1000)
            print(f"Finished total events {total_events} before timestamp {before_timestamp} after timestamp {after_timestamp}")
    else:
        print("Unable to connect to partners.dnaspaces.io. Status code", r.status_code)
else:
    print("Please set environment variable TOKEN before running.")