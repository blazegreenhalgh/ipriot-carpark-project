from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location, capacity, license_plates=None, displays=None, sensor=None, cars=None):
        self.location = location
        self.capacity = capacity
        self.filled_bays = len(self.cars)
        self.available_bays = capacity - self.filled_bays
        self.license_plates = license_plates or []
        self.displays = displays or []
        self.sensor = sensor or []
        self.cars = cars or []

    def __str__(self):
        return f"{self.location} carpark has a max capacity of {self.capacity}"

    def update_plate_database(self, car):
        if car._license_plate in self.license_plates:
            self.license_plates.remove(car._license_plate)
        else:
            self.license_plates.append(car._license_plate)
        self.update_displays()


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


