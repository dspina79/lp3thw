# Printing with Escape Characters
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\on a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("This has a \rcarriage return.")
print("This uses a \abell.")
print("This uses \fform feed.")
print("This has a \vvertical tab.")
print("And this has nothing.")
print("I just backspaced\b\b\b over backspace.")