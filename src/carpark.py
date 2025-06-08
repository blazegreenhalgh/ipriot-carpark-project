class CarPark:
    def __init__(self, location, capacity, filled_bays, available_bays, license_plates=None, displays=None, sensors=None, cars=None):
        self.location = location
        self.capacity = capacity,
        self.filled_bays = filled_bays
        self.available_bays = available_bays
        self.license_plates = license_plates
        self.displays = displays
        self.sensors = sensors
        self.cars = cars

    def __str__(self):
        return f"{self.location} carpark has a max capacity of {self.capacity}"

    def log_license_plates(self, new_license_plates):
        ... # Come back to this and figure it out

    def update_bay_count(self):
        ... # Come back to this and figure it out

    def update_displays(self):
        ... # Come back to this and figure it out



