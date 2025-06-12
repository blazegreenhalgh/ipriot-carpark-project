class Display:
    def __init__(self, id, carpark):
        self.id = id
        self.carpark = carpark

    def __str__(self):
        return f"Display {self.id}: Welcome to the {self.carpark.location} carpark."
    
    def update(self, data):
        for key, value in data:
            print(f"{key}: {value}")

