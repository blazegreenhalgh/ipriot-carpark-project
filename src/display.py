class Display:
    def __init__(self, weather, id, carpark, message="", is_on=False):
        self.weather = weather
        self.id = id
        self.carpark = carpark
        self.is_on = is_on
        self.message = message

    def __str__(self):
        return f"Display {self.id}: Welcome to the {self.carpark.location} carpark."

    def display_bays(self, available_bays):
        # Minimal idea presented here.
        print(f"{available_bays} available") 

