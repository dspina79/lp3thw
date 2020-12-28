# Reading and Writing to Files

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit Ctrl-C (^C).")
print("If you do want that, hit enter a the command prompt.")

input(">")
print("Opening the file...")

# if the 'w' is not provided, then the file is not 
# available for writing
target = open(filename, 'w')

print("Truncating the file. Good-bye!")
target.truncate()

print("Now I'm going to ask you to add three lines to the file.")

line1 = input("Line 1> ")
line2 = input("Line 2> ")
line3 = input("Line 3> ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"Now, we are going to close {filename}")
target.close()