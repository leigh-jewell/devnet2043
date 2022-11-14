# Refer to https://partners.dnaspaces.io/partner/ for creation of 3rd party apps for Cisco DNA Spaces
# This gist shows how to get the firehose events with grpc in Python
# You will need to get the CA cert via openssl - echo | openssl s_client -servername partners.dnaspaces.io -connect \
# partners.dnaspaces.io:443|sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > CA.pem
import grpc
import dna_spaces_pb2
import dna_spaces_pb2_grpc
from prettytable import PrettyTable
from os import environ


api_key = "some-key-here"

def run():
    if 'TOKEN' in environ:
        token = environ['TOKEN']
        print(f"Got token {token}")
        metadata = [('x-api-key', api_key)]
        with open('CA.pem', 'rb') as f:
            credentials = grpc.ssl_channel_credentials(f.read())
        with grpc.secure_channel('partners.dnaspaces.io:443', credentials) as channel:
            stub = dna_spaces_pb2_grpc.FirehoseStub(channel)
            events = stub.GetEvents(dna_spaces_pb2.EventsStreamRequest(), metadata=metadata)
            i = 0
            t = PrettyTable(['spaces_tenant_name', 'mac_address', 'x_pos', 'y_pos', 'confidence_factor'])
            for event in events:
                i += 1
                if event.event_type != dna_spaces_pb2.EventType.KEEP_ALIVE:
                    t.add_row([event.spaces_tenant_name,
                               event.device_location_update.device.mac_address,
                               f'{event.device_location_update.x_pos:.2f}',
                               f'{event.device_location_update.y_pos:.2f}',
                               event.device_location_update.confidence_factor])
                if i > 10:
                    break
            print(t)


if __name__ == '__main__':
    print("Start.")
    run()