class Display:
    def __init__(self, id, carpark):
        self.id = id
        self.carpark = carpark

    def __str__(self):
        return f"Display {self.id}: Welcome to the {self.carpark.location} carpark."
    

    def display_data(self, key, value):
        key = key.replace(key[0], key[0].upper(), 1) # idk if its beautiful or an abomination
        key = key.replace("_", " ")
        print(f"{key} at {self.carpark} carpark: {value}")
        return (f"{key} at {self.carpark} carpark: {value}") # For unit tests

class ColouredDisplay(Display):
    colours = {
        "green": {"start": '\x1b[6;30;42m', "end": '\x1b[0m'},
        "yellow": {"start": "\33[43m", "end": "\33[0m"}
    }

    def __init__(self, id, carpark):
        super().__init__(id, carpark)

    def display_data(self, key, value):
        key = key.replace(key[0], key[0].upper(), 1) # idk if its beautiful or an abomination
        key = key.replace("_", " ")
        if key == "Available bays" and value < 3:
            print(f"{key} at {self.carpark} carpark: {self.colours["yellow"]["start"]} {value} {self.colours["yellow"]["end"]}")
        else:
            print(f"{key} at {self.carpark} carpark: {self.colours["green"]["start"]} {value} {self.colours["green"]["end"]}")
        return (f"{key} at {self.carpark} carpark: {value}") # For unit tests
