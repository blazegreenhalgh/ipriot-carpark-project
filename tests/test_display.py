import unittest
from display import Display
from carpark import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.carpark = CarPark("Russia", 25)
        self.display = Display(1, self.carpark)


    def test_display_initialised_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.carpark, self.carpark)

    def test_display_formatting_correctly(self):
        self.assertEqual(self.display.display_data("available_bays", 30), "Available bays: 30")

    def test_error_when_wrong_argument_in_carpark_update_display(self):
        with self.assertRaises(ValueError):
            self.carpark.update_display("time", 1255)
         
