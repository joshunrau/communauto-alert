from __future__ import annotations
import json

import time

from .cli import parse_args
from .core import get_available_vehicles, get_closest_vehicle
from .vehicle import Vehicle
from .notifications import Notifications
from apprise import NotifyType

def main() -> None:
    args = parse_args()
    notifications = Notifications(args.notify)
    print('Sending a test notification to ensure your configuration is valid...')
    notifications.apobj.notify(
        title = 'Looking for vehicles in ' + args.province,
        body  = 'Starting now...',
    )
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
                title = f"Found Vehicle at {round(distance, 2)} Meters!"
                print(title)
                print(closest_vehicle)
                notifications.apobj.notify(
                    title = title,
                    body  = json.dumps(closest_vehicle.describe()),
                    notify_type = NotifyType.SUCCESS
                )
                return None
        print(f"Failed to find any vehicles. Will check again in {args.interval}s")
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
