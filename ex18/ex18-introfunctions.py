# Names, Variables, Code, Functions

# function taking one or more arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# function taking two definitive arguments
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# function with one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# function with no arguments
def print_none():
    print("Nothing was received.")

# basic calculations for practice
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def print_add(x, y):
    sum = add(x, y)
    print(f"The sum of {x} and {y} is {sum}.")

def print_multiply(x, y):
    product = multiply(x, y)
    print(f"The product of {x} and {y} is {product}.")

print_two("Dean", "Anips")
print_two_again("Dean", "Phillips")
print_one("First!")
print_none()

# do the additional math
print_add(5, 6)
print_multiply(5, 6)    