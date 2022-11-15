import argparse
import time

from importlib.metadata import version

from .bell import Bell
from .vehicles import Vehicles

def main() -> None:
    parser = argparse.ArgumentParser(prog='communauto-alert', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {version('communauto-alert')}")
    parser.add_argument('latitude', help='your latitude', type=float)
    parser.add_argument('longitude', help='your longitude', type=float)
    parser.add_argument('--max_distance', help='max distance of vehicle in meters', default=500, metavar='', type=int)
    args = parser.parse_args()

    bell = Bell()
    vehicles = Vehicles()
    while True:
        vehicles.fetch()
        closest_vehicle = vehicles.get_closest(args.latitude, args.longitude)
        if closest_vehicle:
            distance = closest_vehicle.distance(args.latitude, args.longitude)
            if args.max_distance > distance:
                print('Found Vehicle!')
                bell.play_sync()
                return None
        time.sleep(60)
