from carpark import CarPark

class Car:
    def __init__(self, license_plate, carpark, entry_time=None, exit_time=None, parked_in_bay=False):
        self.license_plate = license_plate
        self.carpark = carpark
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.parked_in_bay = parked_in_bay

    def park(self, carpark):
        if not isinstance(carpark, CarPark):
            raise TypeError("Must park in a CarPark!")
        if self.parked_in_bay == True and self.carpark != carpark:
            raise ValueError("Car already parked in another carpark.")
        else: 
            self.carpark = carpark
            self.parked_in_bay = True

    def exit(self):
        pass
