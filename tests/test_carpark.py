import unittest
from pathlib import Path
from carpark import CarPark
from car import Car
from sensor import Sensor
from display import Display
from datetime import datetime

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.log_file_path = Path("log.txt")
        self.carpark = CarPark("Belmont", 25, log_file = Path(self.log_file_path))
        self.sensor = Sensor(1, self.carpark)
        self.display = Display(2, self.carpark)
        self.car = Car(_license_plate="123")



        

    def test_car_park_initialised_with_all_attributes(self):
        self.assertIsInstance(self.carpark, CarPark)
        self.assertEqual(self.carpark.location, "Belmont")
        self.assertEqual(self.carpark.capacity, 25)
        self.assertEqual(self.carpark.available_bays, 25)
        self.assertEqual(self.carpark.license_plates, [])
        self.assertEqual(self.carpark.displays, [])
        self.assertEqual(self.carpark.sensor, [])
        self.assertEqual(self.carpark.log_file, Path(self.log_file_path))
    
    def test_log_file_exists(self):
        self.assertTrue(self.carpark.log_file.exists())

    def test_car_logged_when_entering(self):
        self.car.park(self.carpark)
        self.sensor.scan_car(self.car)
        with self.carpark.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn(f"Car with plate 123 parked at {datetime.now():%Y-%m-%d %H:%M:%S}\n", last_line)

    def test_car_logged_when_exiting(self):
        self.car.park(self.carpark)
        self.sensor.scan_car(self.car)
        self.car.exit()
        self.sensor.scan_car(self.car)
        with self.carpark.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn(f"Car with plate 123 left at {datetime.now():%Y-%m-%d %H:%M:%S}\n", last_line)

    def test_register_sensor(self):
        self.carpark.register_component(self.sensor)
        self.assertIn(self.sensor, self.carpark.sensor)

    def test_register_display(self):
        self.carpark.register_component(self.display)
        self.assertIn(self.display, self.carpark.displays)

    def tearDown(self):
       Path(self.log_file_path).unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
