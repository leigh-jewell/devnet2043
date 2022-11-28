import json
import requests
from os import environ
from prettytable import PrettyTable

if 'TOKEN' in environ:
    api_key = environ['TOKEN']
    headers = {'X-API-Key': api_key}
    print(f"Using header {headers}")
    r = requests.get('https://partners.dnaspaces.io/api/partners/v1/firehose/events', stream=True, headers=headers)
    if r.status_code == 200:
        print(f"Got status code {r.status_code} from https://partners.dnaspaces.io/api/partners/v1/firehose/events'")
        t = PrettyTable(['mac_address', 'x_pos', 'y_pos'])
        i = 0
        for line in r.iter_lines():
            data = json.loads(line)
            if data['eventType'] == "IOT_TELEMETRY":
                # Only interested in the IOT events
                i += 1
                # Keep count of events we receive
                print(f"Event[{i}]{json.dumps(data['iotTelemetry'], indent=4)}")
                # Print out the IOT_TELEMETRY
                mac = data['iotTelemetry']['deviceInfo']['deviceMacAddress']
                try:
                    x_pos = data['iotTelemetry']['detectedPosition']['xPos']
                    y_pos = data['iotTelemetry']['detectedPosition']['yPos']
                    t.add_row([mac, round(x_pos), round(y_pos)])
                except ValueError:
                    print(f"No position for {mac}")
                if i > 100:
                    # Once we have seen 20 IOT_TELEMETRY events we will break out of the for loop
                    break
            elif data['eventType'] == "KEEPALIVE":
                print(".", end='')
        print(t)
    else:
        print("Unable to connect to partners.dnaspaces.io. Status code", r.status_code)
else:
    print("Please set environment variable TOKEN before running.")