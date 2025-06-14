import unittest
from carpark import CarPark
from car import Car
from sensor import Sensor

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.carpark = CarPark("Belmont", 1)
        self.car = Car()
        self.sensor = Sensor(1, self.carpark)

    def test_car_initialised_with_all_attributes(self):
        self.assertIsInstance(self.car, Car)
        self.assertIsNone(self.car.carpark)
        self.assertFalse(self.car.parked_in_bay)

    def test_park(self):
        self.car.park(self.carpark)
        self.assertEqual(self.car.carpark, self.carpark)
        self.assertTrue(self.car.parked_in_bay)

    def test_car_cannot_park_when_carpark_is_full(self):
        self.car.park(self.carpark)
        self.sensor.scan_car(self.car)
        self.second_car = Car()
        with self.assertRaises(ValueError):
            self.second_car.park(self.carpark)

    def test_error_when_trying_to_park_in_invalid_carpark(self):
        with self.assertRaises(TypeError):
            self.car.park(123)

    def test_error_when_parking_in_carpark_while_parked_in_another(self):
        self.car.park(self.carpark)
        second_carpark = CarPark("Armadale", 1)
        with self.assertRaises(ValueError):
            self.car.park(second_carpark)

    def test_error_exiting_when_not_parked(self):
        with self.assertRaises(ValueError):
            self.car.exit()



