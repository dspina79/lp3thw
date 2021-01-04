# Practice of Learned Concepts

print("Let's practice everything.")
print('You\'d nee to know \'bout escapes with \\ that do:')
print('\n new lines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nore comprehend passion from institution
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

def getupperlower(person_name):
    return person_name.upper(), person_name.lower()

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans}, {jars} jars, and {crates} crates.")

start_point = start_point / 10
formula = secret_formula(start_point)
print("We can also do it this way (having an array of elements passed in)")
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

name = input("Enter your name: ")
results = getupperlower(name)
print("The uppercase of your name is {} and the lowercase is {}.".format(*results))
