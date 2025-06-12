from car import Car
from carpark import CarPark
from display import Display
from sensor import Sensor

belmont_carpark = CarPark('Belmont', 3)
red_car = Car()
belmont_display = Display(1, belmont_carpark)
belmont_sensor = Sensor(2, belmont_carpark)


red_car.park(belmont_carpark)
print(f"Red Car's carpark: {red_car.carpark}")
belmont_sensor.scan_car(red_car)
