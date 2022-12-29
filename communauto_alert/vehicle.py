from __future__ import annotations

import dataclasses
from typing import Literal

from geopy.distance import geodesic


@dataclasses.dataclass
class Vehicle:
    booking_status: Literal[0, 1]
    car_brand: str
    car_model: str
    car_no: int
    latitude: float
    longitude: float

    def __str__(self) -> str:
        return "\n".join([f"{k}: {v}" for k, v in self.describe().items()])

    def distance(self, latitude: float, longitude: float) -> float:
        return geodesic((latitude, longitude), (self.latitude, self.longitude)).meters

    def describe(self) -> dict:
        return {
            "Vehicle Number": self.car_no,
            "Make": self.car_brand,
            "Model": self.car_model,
        }
