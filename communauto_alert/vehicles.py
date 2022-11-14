from __future__ import annotations

import copy
import sys

import requests

from geopy.distance import geodesic

from typing import Literal, TypedDict

from .exceptions import InvalidResponseBodyFormatError

class Vehicle(TypedDict):
    BookingStatus: Literal[0, 1]
    CarBrand: str
    CarModel: str
    CarNo: int
    Latitude: float
    Longitude: float


class Vehicles:
    def __init__(self) -> None:
        self._vehicles: list[Vehicle] = []
    
    def __str__(self) -> str:
        return '\n'.join([f"{key}: {value}" for key, value in self.info().items()])
    
    def info(self) -> dict:
        return {
            "Number of Vehicles": len(self.vehicles)
        }

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
    
        required_keys = ["BookingStatus", "CarBrand", "CarModel", "CarNo", "Latitude", "Longitude"]
        for i in range(len(vehicles)):
            try:
                vehicles[i] = {key: value for key, value in vehicles[i].items() if key in required_keys}
            except (AttributeError, KeyError) as err:
                raise InvalidResponseBodyFormatError from err
        
        self.vehicles = vehicles
    
    def compute_distances(self, latitude: float, longitude: float) -> list[float]:
        """ return a list of the distances, in meters, of all vehicles from the provided coords  """
        distances = []
        for vehicle in self.vehicles:
            user_location = (latitude, longitude)
            vehicle_location = (vehicle["Latitude"], vehicle["Longitude"])
            distances.append(geodesic(user_location, vehicle_location).meters)
        return distances
