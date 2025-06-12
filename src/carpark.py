from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location, capacity, filled_bays, license_plates=None, displays=None, sensor=None, cars=None):
        self.location = location
        self.capacity = capacity
        self.filled_bays = filled_bays
        self.available_bays = capacity - filled_bays
        self.license_plates = license_plates
        self.displays = displays
        self.sensor = sensor
        self.cars = cars

    def __str__(self):
        return f"{self.location} carpark has a max capacity of {self.capacity}"

    def update_plate_database(self, car):
        self.license_plates.append(car.license_plate)
        self.update_displays()

    def remove_license_plate(self, car):
        self.license_plates.remove(car.license_plate)

    def register_component(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Component must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensor.append(component)
            component.carpark = self
        elif isinstance(component, Display):
            self.displays.append(component)
            component.carpark = self

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 25,
        }
        for display in self.displays:
            display.update(data)


