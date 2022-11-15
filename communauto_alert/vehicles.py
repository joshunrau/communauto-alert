from __future__ import annotations

import copy
import dataclasses
import sys
from typing import Literal

import requests
from geopy.distance import geodesic

from .exceptions import InvalidResponseBodyFormatError


@dataclasses.dataclass
class Vehicle:
    booking_status: Literal[0, 1]
    car_brand: str
    car_model: str
    car_no: int
    latitude: float
    longitude: float

    def distance(self, latitude: float, longitude: float) -> float:
        return geodesic((latitude, longitude), (self.latitude, self.longitude)).meters

class Vehicles:
    def __init__(self) -> None:
        self._vehicles: list[Vehicle] = []

    @property
    def vehicles(self) -> list[Vehicle]:
        return self._vehicles
    
    @vehicles.setter
    def vehicles(self, value: list[Vehicle]) -> None:
        self._vehicles = copy.deepcopy(value)
    
    def fetch(self) -> None:
        """ update the list of available vehicles """
        response = requests.get('https://www.reservauto.net/WCF/LSI/LSIBookingServiceV3.svc/GetAvailableVehicles?BranchID=1&LanguageID=1')
        if response.status_code != 200:
            print(f"Failed to fetch vehicles from API, got status code {response.status_code}", file=sys.stderr)
            return None
        
        data = response.json()
        try:
            vehicles = data['d']['Vehicles']
        except KeyError as err:
            raise InvalidResponseBodyFormatError from err
        
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
                    longitude=vehicles[i]["Longitude"]
                )
            except KeyError as err:
                raise InvalidResponseBodyFormatError from err
        
        self.vehicles = vehicles
    
    def get_distances(self, latitude: float, longitude: float) -> list[float]:
        """ return a list of the distances, in meters, of all vehicles from the provided coords  """
        distances = []
        for vehicle in self.vehicles:
            distances.append(vehicle.distance(latitude, longitude))
        return distances
    
    def get_closest(self, latitude: float, longitude: float) -> Vehicle | None:
        """ return the vehicle located closest to the provided coords """
        distances = self.get_distances(latitude, longitude)
        if distances:
            return self.vehicles[distances.index(min(distances))]
        return None