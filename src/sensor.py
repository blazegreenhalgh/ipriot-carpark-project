class Sensor:
    def __init__(self, id, carpark, is_on=False):
        self.id = id
        self.carpark = carpark
        self.is_on = is_on

    def __str__(self):
        return f"Sensor {self.id} is at {self.carpark.location}"

    def scan_car(self, car):
        if car.parked_in_bay == True:
            self.carpark.cars.append(car)
        elif car.parked_in_bay == False:
            self.carpark.cars.remove(car)
        self.carpark.update_plate_database(car.license_plate)

