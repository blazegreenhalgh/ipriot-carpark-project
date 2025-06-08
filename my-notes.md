

# Why Cars and not just plates?
Many reasons; for one, the requirements say it must be *scalable*. Two, it wants to track bays in an *uncontrolled parking lot* meaning that some cars may enter that won't park for whatever reason. Keeping plates within car objects provides an interface(?) for *parking the car*, which then triggers the sensor to scan the plate. This gives a more accurate view of avaiable bays, rather than simply 'total number of plates scanned' dictating this.
Also, it just feels better, ok??? Are we doing this or what???


# Interaction between classes
Car exists (in carpark? or elsewhere...) -> car parks -> sensor notices -> sensor scans license plate -> tells carpark -> carpark stores license plate -> carpark updates total bays -> tells display -> display updates

**Sensor:**
- Notices car parked
- Scans license plate
- Sends to carpark

**Carpark:**
- Stores cars and their plates
- Updates avaiable bays
- Tells display

**Display:**
- Updates display (for available bays)
- Updates display (for weather)
- Updates display (for messages)

# Cars and Carparks
Should there be a method for a car to enter the carpark? And one for them to park? What is the benefit of including the former:
1. Allows for cars to be 'assigned' to carpark, meaning we can have multiple carparks, and the same car can park in each one at different times. Without this, the car having 'parked_in_bay = True' doesn't necessarily mean anything for any particular carpark.
    - Perhaps just need to specify which carpark it has parked into, when it parks - instead of creating a whole extra method for entry. I will do this.
