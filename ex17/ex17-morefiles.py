# More File Operations

# note: Code was commented to reduce the amount of user display on
# a set of simple tasks.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print(f"We are going to copy the contents of {from_file} to {to_file}")
in_file = open(from_file)
in_data = in_file.read()

# print(f"The inpit file is {len(in_data)} bytes long.")
# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C (^C) to abort.")
# input(">")

print(f"Copying {len(in_data)} bytes from {from_file} to {to_file}...")
out_file = open(to_file, 'w')
out_file.write(in_data)

#print("Process complete. Closing files...")

in_file.close()
out_file.close()