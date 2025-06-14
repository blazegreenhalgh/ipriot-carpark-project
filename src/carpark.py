from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime

class CarPark:
    def __init__(self, location, capacity, license_plates=None, displays=None, sensor=None, cars=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.license_plates = license_plates or []
        self.displays = displays or []
        self.sensor = sensor or []
        self.cars = cars or []
        self.log_file = log_file
        self.log_file.touch(exist_ok=True)


    @property
    def available_bays(self):
        return self.capacity - len(self.license_plates)

    def __str__(self):
        return f"{self.location} carpark has a max capacity of {self.capacity}"

    def update_plate_database(self, license_plate):
        if license_plate in self.license_plates:
            self.license_plates.remove(license_plate)
        else:
            self.license_plates.append(license_plate)
        self.update_display("available_bays", self.available_bays)

    def register_component(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Component must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensor.append(component)
            component.carpark = self
        elif isinstance(component, Display):
            self.displays.append(component)
            component.carpark = self

    def update_display(self, key, value):
        # it used to be a dictionary here, but I found it easier to just type two parameters when calling this function - please let me know what is best practice (I have a feeling it's the former)
        if key not in ["temperature", "available_bays", "message"]:
            raise ValueError("Must input temperature, available_bays, or message")
        else:
            for display in self.displays:
                display.display_data(key, value)


    def _log_car_activity(self, car):
        car_action = "parked" if car.parked_in_bay == True else "left"

        with self.log_file.open('a') as file:
            file.write(f"Car with plate {car._license_plate} {car_action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")




