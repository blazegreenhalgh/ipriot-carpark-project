import unittest
from carpark import CarPark
from sensor import Sensor
from display import Display

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.carpark = CarPark("Belmont", 25)
        self.sensor = Sensor(1, self.carpark)
        self.display = Display(2, self.carpark)


        

    def test_car_park_initialised_with_all_attributes(self):
        self.assertIsInstance(self.carpark, CarPark)
        self.assertEqual(self.carpark.location, "Belmont")
        self.assertEqual(self.carpark.capacity, 25)
        self.assertEqual(self.carpark.filled_bays, 0)
        self.assertEqual(self.carpark.available_bays, 25)
        self.assertEqual(self.carpark.license_plates, [])
        self.assertEqual(self.carpark.displays, [])
        self.assertEqual(self.carpark.sensor, [])

    def test_register_sensor(self):
        self.carpark.register_component(self.sensor)
        self.assertIn(self.sensor, self.carpark.sensor)

    def test_register_display(self):
        self.carpark.register_component(self.display)
        self.assertIn(self.display, self.carpark.displays)




if __name__ == "__main__":
    unittest.main()
