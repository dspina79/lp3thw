num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
max_check = int(input("Enter the max check: "))

product = num_1 * num_2
print(f"Product = {product}")
for i in range(1, max_check + 1):
    if (i % num_1 != 0 or i % num_2 != 0) and  i % product == 0:
        print({f"Failed on {i}"})

print("Done")
