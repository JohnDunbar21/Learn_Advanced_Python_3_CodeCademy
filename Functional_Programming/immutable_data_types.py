from collections import namedtuple

# Checkpoint 1 code goes here.
"""
Creating a namedtuple object and instantiating its attributes
"""
country = namedtuple("country", ["name", "capital", "continent"])

# Checkpoint 2 code goes here.
"""
Creating sample tuples using the namedtuple object defined above
"""
france = country("France", "Paris", "Europe")
japan = country("Japan", "Tokyo", "Asia")
senegal = country("Senegal", "Dakar", "Africa")

# Checkpoint 3 code goes here.
"""
Packing all the above tuples into a single one that can be accessed later
"""
countries = (france, japan, senegal)