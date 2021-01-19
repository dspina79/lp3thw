# Simple Yields

def weirder_sequence(mod_value):
    current_number = 1
    previous_number = 0
    while True:
        if current_number % mod_value == 0 and current_number > mod_value:
            current_number -= (mod_value - 1)  
        yield current_number
        temp_number = current_number
        current_number = previous_number + current_number
        previous_number = temp_number


def weird_sequence():
    current_number = 1
    previous_number = 0
    while True:
        if current_number % 2 == 0 and current_number > 2:
            current_number -= 1 
        yield current_number
        temp_number = current_number
        current_number = previous_number + current_number
        previous_number = temp_number

def fibonacci():
    current_number = 1
    previous_number = 0

    while True:
        yield current_number
        temp_number = current_number
        current_number = previous_number + current_number
        previous_number = temp_number


for fib in fibonacci():
    if fib > 10000:
        break
    print(fib)

for ws in weirder_sequence(3):
    if ws > 10000:
        break
    print(ws)

