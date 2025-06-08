from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location, capacity, filled_bays, license_plates=None, displays=None, sensors=None, cars=None):
        self.location = location
        self.capacity = capacity,
        self.filled_bays = filled_bays
        self.available_bays = capacity - filled_bays
        self.license_plates = license_plates
        self.displays = displays
        self.sensors = sensors
        self.cars = cars

    def __str__(self):
        return f"{self.location} carpark has a max capacity of {self.capacity}"

    def register_car_parked(self, car):
        ... # This method will be triggered when the sensor notices a car parked in this carpark.
            # This method will add the car to this carparks list and update the bay availability.

    def register_component(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Component must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def update_displays(self):
        ... # Come back to this and figure it out



