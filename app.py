from flask import Flask, render_template, request
import requests
import json
from datetime import datetime
from os import environ

app = Flask(__name__)

def timestamp_to_date(timestamp):
    try:
        date = datetime.fromtimestamp(timestamp / 1000)
    except OSError:
        date = "No Date"
    return str(date)


def validate_token(check_token):
    return True


def process_iot_data(iot_data):

    ble_mac_list = []
    ble_mac_names = {}
    ble_tags = {}
    ble_count = 0
    tag_updates = []
    ble_mac_str = ""

    ble_count = ble_count + 1
    device_id = data['iotTelemetry']['deviceInfo']['deviceMacAddress']
    # Only grab details for tags we are interested in
    if 'iBeacon' not in data['iotTelemetry']:
        print(data)
        ble_tags[device_id]['x'] = data['iotTelemetry']['detectedPosition']['xPos']
        ble_tags[device_id]['y'] = data['iotTelemetry']['detectedPosition']['yPos']
        ble_tags[device_id]['floor'] = data['iotTelemetry']['location']['name']
        # Some tags only provide extra telemetry data so we need to check
        if 'temperature' in data['iotTelemetry']:
            ble_tags[device_id]['temperature'] = \
                round(data['iotTelemetry']['temperature']['temperatureInCelsius'], 1)
        if 'illuminance' in data['iotTelemetry']:
            ble_tags[device_id]['illuminance'] = \
                data['iotTelemetry']['illuminance']['value']
        if 'airPressure' in data['iotTelemetry']:
            ble_tags[device_id]['airPressure'] = \
                data['iotTelemetry']['airPressure']['pressure']
        if 'carbonEmissions' in data['iotTelemetry']:
            ble_tags[device_id]['carbonEmissions'] = \
                data['iotTelemetry']['carbonEmissions']['co2Ppm']
        if 'battery' in data['iotTelemetry']:
            ble_tags[device_id]['battery'] = data['iotTelemetry']['battery']['value']
        if 'accelerometer' in data['iotTelemetry']:
            ble_tags[device_id]['accelerometer'] = \
                timestamp_to_date(data['iotTelemetry']['accelerometer']['lastMovementTimestamp'])
        if 'pirTrigger' in data['iotTelemetry']:
            pir_trigger = timestamp_to_date(data['iotTelemetry']['pirTrigger']['timestamp'])
            if 'pirTrigger' in ble_tags[device_id].keys():
                if ble_tags[device_id]['pirTrigger'] < pir_trigger:
                    print("NEW PIR date to", pir_trigger)
                    ble_tags[device_id]['pirTrigger'] = pir_trigger
            else:
                ble_tags[device_id]['pirTrigger'] = pir_trigger
                record_timestamp = timestamp_to_date(data['recordTimestamp'])
                print("First PIR update", record_timestamp, device_id,
                      ble_tags[device_id]['pirTrigger'])
        if 'deviceRtcTime' in data['iotTelemetry']:
            ble_tags[device_id]['clock'] = timestamp_to_date(data['iotTelemetry']['deviceRtcTime'])
        if device_id not in tag_updates:
            tag_updates.append(device_id)

    return


@app.route('/', methods=['GET', 'POST'])
def get_ble_telemetry_data():
    # Grab the start time so we know how long to run for.
    start_time = datetime.now()
    process_time_secs = 0.0
    max_wait_secs = 20
    #
    if 'TOKEN' in environ:
        # Get the token from environment variable if we can.
        token = environ['TOKEN']
    else:
        print("Please set the environment TOKEN.")
        token = ""
    if request.method == 'GET':
        # Send blank page just with token.
        return render_template('index.html', api_token=token, ble_tags={})
    elif request.method == 'POST':
        token = request.form.get('api_token')
        print(f"Using token {token} for firehose connection.")
        headers = {'X-API-Key': token}
        # Connect to API
        stream_api = requests.get('https://partners.dnaspaces.io/api/partners/v1/firehose/events',
                                  stream=True, headers=headers)

        if stream_api.status_code == 200:
            error="OK"
            # Read in an update from Firehose API
            for line in stream_api.iter_lines():
                # We just con
                data = json.loads(line)
                if data['eventType'] == "IOT_TELEMETRY":
                    # Only process IOT events
                    process_iot_data(data)
                # Only grab 10 IOT updates
                process_time_secs = round((datetime.now() - start_time).total_seconds(), 1)
                if process_time_secs > max_wait_secs:
                    # Check how long we have been processing requests for.
                    print('Complete. Time taken', process_time_secs)
                    break
        else:
            # Didn't get an ok status, check the status of the request to Firehose.
            print(f"Error in Firehose request got the response {stream_api.status_code} {stream_api.reason}")
            error = stream_api.reason
        return render_template('index.html', ble_tags=ble_tags, time_taken=process_time_secs, api_token=token,
                               error=error)


if __name__ == '__main__':
    app.run()
