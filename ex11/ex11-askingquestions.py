# Asking Questions - Input
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So you are {age} years old, {height} inches tall, and {weight} pounds.")

# added this for extra credit
if weight > "200":
    print("You may need to lose some weight.")
