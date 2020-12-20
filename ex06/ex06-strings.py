# Strings and text

types_of_people = 10
# interpolates the types_of_people variable into the string
x = f"There are {types_of_people} types of people."

# new variables and inerpolation
binary = "binary"
do_not = "don't"
y = f"Those that understand {binary} and those who {do_not}."

# printing
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

# identification of new variables
hilarious = False
# creating a string with an interpoliation placeholder that is unnamed.
joke_evaluation = "Isn't that joke so funny?! {}"
# applies argument as the interpolation
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string wtih a right side"

# summing strings
print(w + e)