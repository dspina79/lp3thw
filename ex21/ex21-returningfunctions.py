# Returning Functions

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def bruteForcePrimeCheck(a):
    if (a % 2 == 0 and a != 2) or a == 0 or a == 1:
        return False
    
    check_num = 3
    while check_num < a:
        if a % check_num == 0:
            return False
        check_num += 2
    
    return True

print("Let's do some math with functions.")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for extra credit
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do that by hand?")

num_to_check = int(input("Check a number to see if it's prime: "))
print(f"Using brute force, is {num_to_check}? {bruteForcePrimeCheck(num_to_check)}")
