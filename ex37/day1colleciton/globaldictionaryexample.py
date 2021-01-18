# Code to use as many Python keywords and contructs.

cube = lambda x: x ** 3
user_name = ""

def getUserValues():
    global user_name
    print(f"Greetings\n.Please enter your name at the cursor below.")
    user_name = input("\\> ")

def run_code():
    code = input("Enter in a simple print command or other Python code: ")
    exec(code)

def generate_person_dictionary(first_name, last_name, age, favorite_color):
    return {'first_name': first_name, 'last_name': last_name, 'age': age, 'favorite_color' : favorite_color}


def print_person_dictionary(person_dict):
    print(f"First Name: {person_dict['first_name']}\tLast Name: {person_dict['last_name']}")
    print(f"Age: {person_dict['age']}")
    print(f"Their Favorite Color: {person_dict['favorite_color']}")
    
def get_average(list_numbers):
    size = 0
    total = 0
    for num in list_numbers:
        total += num
        size += 1
    
    if size == 0:
        raise "You provided an empty set."

    return float(total)/float(size)

def print_escape_character_output():
    escape_characters = {'slash' : "\\", 'double-quote': "\"", 'a': "\a", 'b': "\b", 'f': "\f", 't': "\t", 'v' : "\v"}
    for key in escape_characters.keys():
        print_string = "print('When using " + key + ", the output is This is the text before " + escape_characters[key] +  " and after the escampe character.')"
        exec(print_string)

getUserValues()
#run_code()
person = generate_person_dictionary("Dean", "Anips", 35, "Green")
print_person_dictionary(person)
list_numbers = [1,2,3,4,5,6,7,8,9,10]
print(f"The average of {list_numbers} is {get_average(list_numbers)}.")
number_to_cube = int(input("Provide a number to cube: "))
print(f"The cube of {number_to_cube} is {cube(number_to_cube)}.")
print_escape_character_output()