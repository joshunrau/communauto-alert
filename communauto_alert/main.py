import argparse
import time

from importlib.metadata import version

from .bell import Bell
from .vehicles import Vehicles

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='communauto-alert', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {version('communauto-alert')}")
    parser.add_argument('latitude', help='your latitude', type=float)
    parser.add_argument('longitude', help='your longitude', type=float)
    parser.add_argument('--interval', help='interval between checks in seconds', default=60, metavar='', type=int)
    parser.add_argument('--max_distance', help='max distance of vehicle in meters', default=500, metavar='', type=int)
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    
    bell = Bell()
    vehicles = Vehicles()
    while True:
        vehicles.fetch()
        print(f'Checking for vehicles within radius of {args.max_distance} meters...')
        closest_vehicle = vehicles.get_closest(args.latitude, args.longitude)
        if closest_vehicle:
            distance = closest_vehicle.distance(args.latitude, args.longitude)
            if args.max_distance > distance:
                print('Found Vehicle!')
                bell.play_sync()
                return None
        print(f'Failed to find any vehicles. Will check again in {args.interval}s')
        time.sleep(args.interval)
