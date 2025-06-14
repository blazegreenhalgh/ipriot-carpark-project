import unittest
from carpark import CarPark
from car import Car
from sensor import Sensor
from display import Display
from datetime import datetime

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.carpark = CarPark("Belmont", 1)
        self.car = Car()
        self.sensor = Sensor(1, self.carpark)
        self.display = Display(1, self.carpark)
        self.carpark.register_component(self.sensor)
        self.carpark.register_component(self.display)

    def test_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.sensor, Sensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.carpark, self.carpark)

    def test_car_scanned_when_parked(self):
        self.car.park(self.carpark)
        self.sensor.scan_car(self.car)
        self.assertIn(self.car, self.carpark.cars)
        self.assertIn(self.car._license_plate, self.carpark.license_plates)

    def test_car_exit_successfully(self):
        self.car.park(self.carpark)
        self.sensor.scan_car(self.car)
        self.car.exit()
        self.sensor.scan_car(self.car)
        self.assertEqual(self.car.parked_in_bay, False)
        self.assertFalse(self.car in self.carpark.cars)
