# Reading a File
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
txt.close() # close the file after being done with it.

print("Type the filename again or pick a nwe one: ")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()