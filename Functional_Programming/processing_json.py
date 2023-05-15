import json
from collections import namedtuple
from functools import reduce

city = namedtuple("city", ["name", "country", "coordinates", "continent"])

with open('Functional_Programming\\Data_Files\\cities.json') as json_file:
  data = json.load(json_file) 

cities = map(lambda x: city(x["name"], x["country"], x["coordinates"], x["continent"]), data["city"])

# Code for Checkpoint 1 goes here.
asia = tuple(filter(lambda x: x.continent == "Asia", cities))
print(asia)

west = None

# Code for Checkpoint 2 goes here.
west = tuple(reduce(lambda x, y: x if x.coordinates[1] < y.coordinates[1] else y, asia))
print(west)