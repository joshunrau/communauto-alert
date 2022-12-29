from __future__ import annotations

import requests

from typing import get_type_hints

from .vehicle import Vehicle

API_URL = "https://www.reservauto.net/WCF/LSI/LSIBookingServiceV3.svc/GetAvailableVehicles?BranchID=1&LanguageID=1"
VALID_FILTERS = list(get_type_hints(Vehicle).keys())


class InvalidResponseBodyFormatError(Exception):
    def __init__(self) -> None:
        super().__init__(
            "Invalid response body format. This likely means Communauto has changed their API."
        )


def get_available_vehicles() -> list[Vehicle]:
    """get a list of all vehicles"""
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to fetch vehicles from API, got status code {response.status_code}"
        )

    data = response.json()
    try:
        vehicles = data["d"]["Vehicles"]
    except KeyError as err:
        raise InvalidResponseBodyFormatError

    if not isinstance(vehicles, list):
        raise InvalidResponseBodyFormatError

    for i in range(len(vehicles)):
        try:
            vehicles[i] = Vehicle(
                booking_status=vehicles[i]["BookingStatus"],
                car_brand=vehicles[i]["CarBrand"],
                car_model=vehicles[i]["CarModel"],
                car_no=vehicles[i]["CarNo"],
                latitude=vehicles[i]["Latitude"],
                longitude=vehicles[i]["Longitude"],
            )
        except KeyError as err:
            raise InvalidResponseBodyFormatError from err

    return vehicles


def compute_distances(
    vehicles: list[Vehicle], latitude: float, longitude: float
) -> list[float]:
    """return a list of the distances, in meters, of vehicles from the provided coords"""
    distances = []
    for vehicle in vehicles:
        distances.append(vehicle.distance(latitude, longitude))
    return distances


def get_closest_vehicle(
    vehicles: list[Vehicle], latitude: float, longitude: float
) -> Vehicle | None:
    """return the vehicle located closest to the provided coords"""
    distances = compute_distances(vehicles, latitude, longitude)
    if distances:
        return vehicles[distances.index(min(distances))]
    return None
