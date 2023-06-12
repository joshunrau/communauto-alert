from __future__ import annotations

import time

from .bell import Bell
from .cli import parse_args
from .core import get_available_vehicles, get_closest_vehicle
from .vehicle import Vehicle


def main() -> None:
    args = parse_args()
    bell = Bell()
    vehicles: list[Vehicle] = []
    while True:
        print(f"Checking for vehicles within radius of {args.max_distance} meters...")
        vehicles = get_available_vehicles(args.province)
        if args.no_prius:
            vehicles = list(filter(lambda v: v.car_model != "Prius C", vehicles))
        closest_vehicle = get_closest_vehicle(vehicles, args.latitude, args.longitude)
        if closest_vehicle:
            distance = closest_vehicle.distance(args.latitude, args.longitude)
            if args.max_distance > distance:
                print("Found Vehicle!")
                print(f"Distance: {round(distance, 2)} Meters")
                print(closest_vehicle)
                bell.play_sync()
                return None
        print(f"Failed to find any vehicles. Will check again in {args.interval}s")
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
