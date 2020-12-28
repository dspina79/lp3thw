# Exercise 16 Challenge

from sys import argv
script, filename = argv

print(f"""
The file, {filename} is about to be cleared. 
Press Enter to continue.
""")

input(">")

target = open(filename, 'w')


print("Now enter three new lines")
line1 = input("1>")
line2 = input("2>")
line3 = input("3>")

target.write(f"""
{line1}
{line2}
{line3}
""")

print("Done, closing the file")
target.close()
