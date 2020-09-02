# ! python3
# quick_weather.py - Prints the weather for a location from the command line.

import json, requests, sys

# compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quick_weather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from open_weather_map.org's API.
api_key = 'e0fdef6f7ea34e1905622d6a9126f08f'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
url = base_url + 'appid=' + api_key + "&q=" + location

response = requests.get(url)
response.raise_for_status()

# Load JSON data into Python variable .
weather_data = json.loads(response.text)
# Print weather descriptions.
w = weather_data
print('Current weather in %s: ' % location)
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])
print('{0}'.format(location) + '\'s humidity is:')
print(w['main']['humidity'])

