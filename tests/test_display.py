import unittest
from display import Display
from carpark import CarPark
from car import Car
from sensor import Sensor

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.carpark = CarPark("Russia", 25)
        self.display = Display(1, self.carpark)
        self.car = Car()
        self.sensor = Sensor(1, self.carpark)


    def test_display_initialised_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.carpark, self.carpark)

    def test_display_formatting_correctly(self):
        self.assertEqual(self.display.display_data("available_bays", 30), "Available bays: 30")

    def test_display_accurate_bay_count(self):
        self.car.park(self.carpark)
        self.sensor.scan_car(self.car)
        self.assertEqual(self.display.display_data("available_bays", 29), "Available bays: 29")


    def test_error_when_wrong_argument_provided_to_display(self):
        with self.assertRaises(ValueError):
            self.carpark.update_display("time", 1255)
         
