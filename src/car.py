from carpark import CarPark
import random

class Car:
    def __init__(self, carpark=None, entry_time=None, exit_time=None, parked_in_bay=False):
        self._license_plate = self._initiate_license_plate()
        self.carpark = carpark
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.parked_in_bay = parked_in_bay

    def _initiate_license_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d") 

    def park(self, carpark):
        if not isinstance(carpark, CarPark):
            raise TypeError("Must park in a CarPark!")
        if self.parked_in_bay == True and self.carpark != carpark:
            raise ValueError("Car already parked in another carpark.")
        if carpark.available_bays <= carpark.capacity:
            self.carpark = carpark
            self.parked_in_bay = True
        else:
            raise ValueError("I can't go park, carpark is full!")

    def exit(self):
        if not self.parked_in_bay:
            raise ValueError("Not parked!")
        else:
            self.carpark = None
            self.parked_in_bay = False

