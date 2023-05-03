#!/usr/bin/python3
# import requests
#
# response = requests.get('https://swapi.dev/api/people/1/')
# data = response.json()
#
# print(data['name'])
import requests

url = 'https://swapi.dev/api/people/'
data = []

while url:
    response = requests.get(url)
    results = response.json()['results']
    data.extend(results)
    url = response.json()['next']

for character in data:
    print(character['name'])
