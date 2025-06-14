
class Sensor:
    def __init__(self, id, carpark):
        self.id = id
        self.carpark = carpark

    def __str__(self):
        return f"Sensor {self.id} is at {self.carpark.location}"

    def scan_car(self, car):
        if car.parked_in_bay == True:
            self.carpark.cars.append(car)
        elif car.parked_in_bay == False:
            self.carpark.cars.remove(car)

        self.carpark.update_plate_database(car._license_plate)
        self.carpark._log_car_activity(car)

