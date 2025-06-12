from datetime import datetime

class Sensor:
    def __init__(self, id, carpark):
        self.id = id
        self.carpark = carpark

    def __str__(self):
        return f"Sensor {self.id} is at {self.carpark.location}"

    def scan_car(self, car):
        if car.parked_in_bay == True:
            self.carpark.cars.append(car)
            car.entry_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        elif car.parked_in_bay == False:
            car.exit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.carpark.update_plate_database(car._license_plate)

