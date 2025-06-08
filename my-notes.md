

# Why Cars and not just plates?
Many reasons; for one, the requirements say it must be *scalable*. Two, it wants to track bays in an *uncontrolled parking lot* meaning that some cars may enter that won't park for whatever reason. Keeping plates within car objects provides an interface(?) for *parking the car*, which then triggers the sensor to scan the plate. This gives a more accurate view of avaiable bays, rather than simply 'total number of plates scanned' dictating this.
Also, it just feels better, ok??? Are we doing this or what???



## Sensors and cars
Car exists (in carpark? or elsewhere...) -> car parks -> sensor notices -> sensor scans license plate -> tells carpark -> carpark stores license plate -> carpark updates total bays -> tells display -> display updates
