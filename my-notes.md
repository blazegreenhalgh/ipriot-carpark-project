

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
 



 # Debugging
Issue when testing: test_sensor, testing that cars exit time is tracked when scanned out. I tested it, and it failed, saying it could not list.remove as it's not in the list (of carpark.cars). I couldn't figure this out - why was it saying it can't remove it. I added to my previous test (scanning the car in) to make sure the car was logged in the carpark when entering. It was. I then reviewed the code in the Sensor class and noticed, I was removing it from the scan_car function, and also calling the Carpark to update it's database - effectively trying to remove it twice. After removing the former line of code, it worked! 
This also made me realise that my test case was too narrow - my exit timestamp test failed, not because of the timestamp, but because of another issue. I think my test should be broader, as the timestamp is one aspect of scanning the car out, I should be testing that as a whole.
