
### TrafficLIVE

A Python wrapper of the TrafficLIVE API.

This is currently in pre-alpha. I have some of the basic endpoints wrapped. Adding new functions should be really easy, so please send me a pull request.


### Usage

See the tests for examples. But, effectively:

   import trafficlive.trafficlive as tl

   server = tl.TrafficLive("email@address", "api-token")
   employess = server.get_employees()

All functions will return a data structure as per the [TrafficLive documentation](http://46.18.86.57/_documentation/api/).
