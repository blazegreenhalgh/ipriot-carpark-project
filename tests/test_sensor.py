import unittest
from carpark import CarPark
from car import Car
from sensor import Sensor

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.carpark = CarPark("Belmont", 1)
        self.car = Car()
        self.sensor = Sensor(1, self.carpark)

    def test_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.sensor, Sensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.carpark, self.carpark)

    def test_car_scanned_when_parked(self):
        self.car.park(self.carpark)
        self.sensor.scan_car(self.car)
        self.assertEqual(self.carpark.filled_bays, 1)
        self.assertIn(self.car._license_plate, self.carpark.license_plates)


