import unittest

from communauto_alert.vehicles import Vehicles

class TestVehicles(unittest.TestCase):
    def test_fetch(self) -> None:
        vehicles = Vehicles()
        vehicles.fetch()
        self.assertTrue(len(vehicles.vehicles) > 0)
