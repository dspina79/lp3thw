# More Variable Definitions

name = 'Dean Anips'
age = 41
height = 74 #inches
eyes = 'brown'
teeth = 'white'
hair = 'dark brown'
weight = 220.0
weight_kg = round(weight / 2.2)
height_cm = round(height * 2.54)

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's a bit too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usally {teeth} depending on the coffee.")
print(f"If we were using metric, his height would be {height_cm}cm and {weight_kg}kg.")
# sum up some values
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")