class Sensor:
    def __init__(self, id, carpark, is_on=False):
        self.id = id
        self.carpark = carpark
        self.is_on = is_on

    def __str__(self):
        return f"Sensor {self.id} is at {self.carpark.location}"

    def scan_parked_car(self, car):
        if car.carpark == self.carpark:
            return car.license_plate # something like this

    def scan_car_exit(self, car): 
        pass 

