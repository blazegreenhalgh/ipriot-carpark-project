from carpark import CarPark
import random

class Car:
    def __init__(self, _license_plate=None, carpark=None, parked_in_bay=False):
        self._license_plate = _license_plate or self._initiate_license_plate()
        self.carpark = carpark
        self.parked_in_bay = parked_in_bay

    def _initiate_license_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d") 

    def park(self, carpark):
        """
        Attributes a carpark to the car, and sets parked_in_bay to True.
        Note: the sensor must scan the car to be added to the carparks database. 

        Args: 
            carpark(obj): The carpark the car will park in. 
        """
        if not isinstance(carpark, CarPark):
            raise TypeError("Must park in a CarPark!")
        if self.parked_in_bay == True and self.carpark != carpark:
            raise ValueError("Car already parked in another carpark.")
        if carpark.available_bays > 0:
            self.carpark = carpark
            self.parked_in_bay = True
        elif carpark.available_bays <= 0:
            raise ValueError("I can't go park, carpark is full!")

    def exit(self):
        if not self.parked_in_bay:
            raise ValueError("Not parked!")
        else:
            self.carpark = None
            self.parked_in_bay = False

