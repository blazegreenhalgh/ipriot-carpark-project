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

