# Refer to https://partners.dnaspaces.io/partner/ for creation of 3rd party apps for Cisco DNA Spaces
# This gist shows how to get the firehose events with grpc in Python
# You will need to get the CA cert via openssl - echo | openssl s_client -servername partners.dnaspaces.io -connect partners.dnaspaces.io:443|sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > CA.pem
# gRPC information reference https://grpc.io/docs/languages/python/quickstart/
# gRPC proto file can be found here: http://partners.dnaspaces.io/resources/dnaspaces_grpc_proto_spec_v1.2.6_standard.proto
#
# TO recompile with proto file:
# python -m grpc_tools.protoc -I./ --python_out=. --pyi_out=. --grpc_python_out=. ./dnaspaces.proto
#
import grpc
import dna_spaces_pb2
import dna_spaces_pb2_grpc
from prettytable import PrettyTable
from os import environ
from datetime import timedelta
from datetime import datetime


def run():
    if 'TOKEN' in environ:
        token = environ['TOKEN']
    else:
        token = input("Please enter TOKEN key: ")
    if len(token) > 0:
        prev_hour = round((datetime.now() - timedelta(hours=1)).timestamp()*1000)

        metadata = [('x-api-key', token)]
        with open('CA.pem', 'rb') as f:
            credentials = grpc.ssl_channel_credentials(f.read())
        with grpc.secure_channel('partners.dnaspaces.io:443', credentials) as channel:
            stub = dna_spaces_pb2_grpc.FirehoseStub(channel)
            events = stub.GetEvents(dna_spaces_pb2.EventsStreamRequest(from_timestamp=prev_hour), metadata=metadata)
            i = 0
            t = PrettyTable(['mac_address', 'x_pos', 'y_pos'])
            for event in events:
                if event.event_type == dna_spaces_pb2.EventType.IOT_TELEMETRY:
                    # Only interested in the IOT events
                    i += 1
                    # Keep count of events we receive
                    print(event)
                    # Print out the IOT_TELEMETRY
                    mac = event.iot_telemetry.device_info.device_mac_address
                    try:
                        x_pos = event.iot_telemetry.detected_position.x_pos
                        y_pos = event.iot_telemetry.detected_position.y_pos
                        t.add_row([mac, round(x_pos), round(y_pos)])
                    except ValueError:
                        print(f"No position for {mac}")
                elif event.event_type == dna_spaces_pb2.EventType.KEEP_ALIVE:
                    print(".", end='')
                if i > 100:
                    # Once we have seen 20 IOT_TELEMETRY events we will break out of the for loop
                    break
            print(t)
    else:
        print("Error: API key too short.")


if __name__ == '__main__':
    run()
