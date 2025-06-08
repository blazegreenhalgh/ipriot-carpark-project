class Display:
    def __init__(self, weather, message="", id, is_on=False):
        self.weather = weather
        self.message = message
        self.id = id
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: Welcome to the carpark."

    def display_bays(self, available_bays):
        # Minimal idea presented here.
        print(f"{available_bays} available") 

