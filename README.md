# Awesome Smart Carpark
This is going to be awesome (maybe)

## Introduction
This is a smart carpark system, that detects the amount of cars parked using a sensor, and displays that information (along with other useful information) on a display. There can be any number of carparks with any number of cars. There are built in error-checks for edge cases.  

## How to Use
### Setup
1. Initialise a Carpark
```python
# Params: location, capacity
# Optional: license_plates, display, sensor, cars, log_file, config_file
moondalup_carpark = CarPark('Moondalup', 3)
```
2. Initialise components 
```python
moondalup_sensor = Sensor(1, moondalup_carpark)
moondalup_display = Display(1, moondalup_carpark)
```

3. Register components with carpark
```python
moondalup_carpark.register_component(moondalup_sensor)
moondalup_carpark.register_component(moondalup_display)
```

4. Initialise cars
```python
car_one = Car()
car_two = Car()
car_three = Car()
# Cars can be inside the carpark without parking (the carpark is uncontrolled).
car_four = Car(carpark=moondalup_carpark)
```

### Parking & Scanning Cars
1. Park and scan car
```python
car_one.park(moondalup_carpark)
moondalup_carpark.sensor.scan_car(car_one)
```

A few things happen: 
- Car is added to Carpark database
- Car license plate is stored in Carpark database
- Car entry time is logged to specified log_file
- Display is updated to show amount of available bays at the carpark it's registered at.

Display shows: 
> Available bays at Moondalup carpark: 2


### Exiting a carpark
```python
car_three.exit()
moondalup_carpark.sensor.scan_car(car_three)
```

- Car `parked_in_bay` is set to `False`
- Sensor removes car + license plate from Carpark database
- Exit time is logged to log_file
---

1. A car cannot park in a carpark if it's already parked elsewhere.
```python
joondalup = CarPark("Joondalup", 3)
belmont = CarPark("Belmont", 5)
car = Car()

car.park(joondalup)
joondalup.sensor.scan_car(car)

car.park(belmont)
⚠️ ERROR: CAR ALREADY PARKED ELSEWHERE
```

### Displays
A display is automatically updated when the Sensor scans a parked car.
You can update the temperature and message shown on the display.
```python
moondalup_carpark.display.display_data("temperature", 37)
moondalup_carpark.display.display_data("message", "It's bloody hot!")
```
A ColouredDisplay can be used, which displays the available bays with a green background if <3, and yellow of >3


### More Carparks!
Any number of carparks can be created, with any number of cars. A car can park at one carpark, and then move to another, and so on and so forth. All of this will be logged in the corresponding log_file for each carpark (or, in one file if both are the same)
