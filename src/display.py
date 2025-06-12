class Display:
    def __init__(self, id, carpark, is_on=False):
        self.id = id
        self.carpark = carpark
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: Welcome to the {self.carpark.location} carpark."
    
    def update(self, data):
        for key, value in data:
            print(f"{key}: {value}")

