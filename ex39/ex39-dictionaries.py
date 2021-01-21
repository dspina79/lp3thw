# Dictionaries

# create a mapping of state to abbrieviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'Albany'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)

print("New York State has: ", cities['NY'])
print("Oregon State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's state abbrieviation is: ", states['Michigan'])
print("Florida's state abbrieviation is: ", states['Florida'])

# print every state abbrieviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbrieviated as {abbrev}.")

# print every city
print('-' * 10)
for state, city in list(cities.items()):
    print(f"{state} has the city, {city}.")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} has the abbrieviation {abbrev} and has the city {cities[abbrev]}.")

print('-' * 10)
# safely get an abbrieviation for a state that might not be there

state = states.get('Texas')

if not state:
    print('Sorry, there is no Texas in the dictionary.')

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state of 'TX' is {city}.")

