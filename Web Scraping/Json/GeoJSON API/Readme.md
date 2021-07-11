In this assignment you will write a Python program that will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. 
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.

To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the 
urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Test Data / Sample Execution:

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ".

Please run your program to find the place_id for this location:

Universidad Central de Venezuela
