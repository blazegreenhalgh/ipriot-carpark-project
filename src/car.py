class Car:
    def __init__(self, license_plate, entry_time=None, exit_time=None, parked_in_bay=False):
        self.license_plate = license_plate
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.parked_in_bay = parked_in_bay

    def park(self):
        pass

    def exit(self):
        pass
