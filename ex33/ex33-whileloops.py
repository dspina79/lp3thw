# While Loops

def generate_array(limit, steps):
    i = 0
    numbers = []
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + steps
        print("Numbers now ", numbers)
        print(f"At the bottom i is {i}.")

    return numbers

def generate_array_for(limit, steps):
    numbers = []
    for i in range(0, limit, steps):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now ", numbers)
        print(f"At the bottom i is {i}.")
    return numbers

limit_value = int(input("How high do you want to go? "))
steps = int(input("Provide the step interval: "))
numbers = generate_array(limit_value, steps)
print("The numbers: ")
for num in numbers:
    print(num)

numbers2 = generate_array_for(limit_value, steps)
for num in numbers2:
    print(num)
