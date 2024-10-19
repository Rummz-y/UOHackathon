import requests
import json

state = "NC"

response = requests.get(f'https://api.weather.gov/alerts/active?area=CA').json()

for x in response['features']:
    print(x['properties']['description'])
    
