# Functions and Files

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

def get_line_count(f):
    rewind(f)
    line_count = 0
    while f.readline():
        line_count += 1
    
    rewind(f)
    return line_count

# start here
current_file = open(input_file)
print("First, let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind to the start of the file.")
rewind(current_file)

print(f"The current line count of {input_file} is {get_line_count(current_file)} lines.")

current_line = 1
max_lines = get_line_count(current_file)
line_count = int(input("How many lines should be output? "))

if line_count > max_lines:
    line_count = max_lines
   
print(f"Writing {line_count} lines...\n")
while current_line <= line_count:
    print_a_line(current_line, current_file)
    current_line += 1

current_file.close()