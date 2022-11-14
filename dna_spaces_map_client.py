import grpc
import dna_spaces_pb2
import dna_spaces_pb2_grpc
from prettytable import PrettyTable
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from point import Point

# StepTracker - sandbox
api_key = "64029EBBAB8443F38570144644E386E4"

# Test stream
# api-key = "2C7B6986A7F24F10ABCA5453B1C7A928"

def run():
    metadata = [('x-api-key', api_key)]
    clients = {}
    with open('CA.pem', 'rb') as f:
        credentials = grpc.ssl_channel_credentials(f.read())
    with grpc.secure_channel('partners.dnaspaces.io:443', credentials) as channel:
        stub = dna_spaces_pb2_grpc.FirehoseStub(channel)
        events = stub.GetEvents(dna_spaces_pb2.EventsStreamRequest(), metadata=metadata)
        i = 0
        t = PrettyTable(['mac_address', 'distance'])
        x = []
        y = []
        for event in events:
            i += 1
            if event.event_type != dna_spaces_pb2.EventType.KEEP_ALIVE:
                x.append(event.device_location_update.x_pos)
                y.append(event.device_location_update.y_pos)
                if event.device_location_update.device.mac_address in clients:
                    clients[event.device_location_update.device.mac_address].append(
                        Point((event.device_location_update.x_pos, event.device_location_update.y_pos)))
                else:
                    clients[event.device_location_update.device.mac_address] = \
                        [Point((event.device_location_update.x_pos, event.device_location_update.y_pos))]
            if i > 1000:
                break
        colours = list(dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS).keys())
        set_colour = []
        for mac in clients:
            x = []
            y = []
            colour = colours.pop()
            distance = 0.0
            first = True
            for point in clients[mac]:
                x.append(point.getX())
                y.append(point.getY())
                set_colour.append(colour)
                if first:
                    prev_point = point
                    first = False
                else:
                    distance += point.distance(prev_point)
            print(mac, distance)
            t.add_row([mac, f'{distance:.2f}'])
            plt.plot(x, y, linestyle='--', marker='o', color=colour)
        plt.show()
        print(t)


if __name__ == '__main__':
    run()
