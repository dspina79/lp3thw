# Basic Revew
# Just come code to highlight previous lessons learned

from sys import argv

script, arg1 = argv


def read_file(f, num_lines_to_read):
    num_lines_total = get_num_lines(f)
    f.seek(0)
    print(f"There are {num_lines_total} total lines.")
    line_num = 1
    while line_num <= num_lines_total and line_num <= num_lines_to_read:
        line = f.readline()
        print(line_num, line)
        line_num += 1
    
    return

def get_num_lines(f):
    f.seek(0)
    line_num = 0
    while f.readline():
        line_num += 1

    return line_num


input_file = open(arg1)
lines_to_read = input('How many lines to read? ')
read_file(input_file, int(lines_to_read))
input_file.close()
