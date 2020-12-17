# Variables

# set variables
cars = 100
# space in a car is handled as floating point
space_in_a_car = 4.0
# number of active drivers
drivers = 30
# number of passengers
passengers = 90

#identfiy the number of non driven cars
cars_not_driven = cars - drivers
# assign value of cars driven to drivers assuming a 1:1 ratio
cars_driven = drivers
# determine carpool capacity
carpool_capacity = cars_driven * space_in_a_car

# calaculate the number of passengers in a car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "passengers in each car.")
