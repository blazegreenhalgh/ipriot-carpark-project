from car import Car
from carpark import CarPark
from display import Display, ColouredDisplay
from sensor import Sensor


moondalup_carpark = CarPark('Moondalup', 3, log_file="moondalup.txt", config_file="moondalup_config.json")
moondalup_carpark.write_config()
moondalup_carpark.from_config(moondalup_carpark.config_file)

# Instantiate and register components
moondalup_sensor = Sensor(1, moondalup_carpark)
moondalup_carpark.register_component(moondalup_sensor)
moondalup_display = Display(1, moondalup_carpark)
moondalup_carpark.register_component(moondalup_display)
print(moondalup_carpark.sensor)

car_one = Car()
car_two = Car()
car_three = Car()
# Cars can be inside the carpark without parking (this is my functionality of the 'uncontrolled' element).
car_four = Car(carpark=moondalup_carpark)

# Car can park, and is scanned when parked.
car_one.park(moondalup_carpark)
moondalup_carpark.sensor.scan_car(car_one)

car_two.park(moondalup_carpark)
moondalup_carpark.sensor.scan_car(car_two)

# Alternative syntax for scanning
car_three.park(moondalup_carpark)
moondalup_sensor.scan_car(car_three)

# car_four is still in the carpark, despite bays being full.
# if attempted to park, would raise an exception.


tyumen = CarPark("Tyumen", 1)
russian_display = ColouredDisplay(1, tyumen)
russian_sensor = Sensor(1, tyumen)
tyumen.register_component(russian_display)
tyumen.register_component(russian_sensor)
russian_car = Car()

russian_car.park(tyumen)
russian_sensor.scan_car(russian_car)
