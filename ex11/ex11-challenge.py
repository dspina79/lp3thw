# Additional Python Form

print("What is your favorite color?", end=' ')
favorite_color = input()
print(f"So you like {favorite_color}. What is another color you like?", end=' ')
second_color = input()
print("If you could like anywhere in the world, where would it be?", end=' ')
place = input()

print(f"""
So, you're favorite colors are {favorite_color} and {second_color}. 
You would prefer to like in {place}. 
That's nice.
""")