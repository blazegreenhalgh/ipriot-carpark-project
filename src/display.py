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

