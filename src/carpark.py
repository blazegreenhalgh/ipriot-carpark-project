from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    def __init__(self, location, capacity, license_plates=None, display=None, sensor=None, cars=None, log_file=Path("log.txt"), config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.license_plates = license_plates or []
        self.display = display
        self.sensor = sensor
        self.cars = cars or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)


    @property
    def available_bays(self):
        return self.capacity - len(self.license_plates)

    def __str__(self):
        return self.location

    def _log_car_activity(self, car):
        car_action = "parked" if car.parked_in_bay == True else "left"
        with self.log_file.open('a') as file:
            file.write(f"Car with plate {car._license_plate} {car_action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def register_component(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Component must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensor = component
            component.carpark = self
        elif isinstance(component, Display):
            self.display = component
            component.carpark = self

    def update_plate_database(self, license_plate):
        if license_plate in self.license_plates:
            self.license_plates.remove(license_plate)
        else:
            self.license_plates.append(license_plate)
        self.update_display("available_bays", self.available_bays)

    def update_display(self, key, value):
        # it used to be a dictionary here, but I found it easier to just type two parameters when calling this function - please let me know what is best practice (I have a feeling it's the former)
        if key not in ["temperature", "available_bays", "message"]:
            raise ValueError("Must input temperature, available_bays, or message")
        else:
            self.display.display_data(key, value)

    def write_config(self):
        with open(self.config_file, "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])





