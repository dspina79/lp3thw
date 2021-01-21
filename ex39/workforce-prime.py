# Workforce Version 1

from os import system, name

# global elements
person_id_index = 1
persons = {}
manager_assignments = {}

class Person:    
    def __init__(self, first, last, title, id):
        self.first_name = first
        self.last_name = last
        self.position = title
        self.id = id

    def display_card(self):
        print(f"{self.last_name}, {self.first_name}")
        print(f"\tID: {self.id}")
        print(f"\tPosition: {self.position}")

    def get_short_description(self):
        return f"{self.last_name}, {self.first_name} ({self.id})"

class ManagerAssignment:
    pass


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def wait_enter():
    print("")
    val = input("Press ENTER to continue.")

def menu_display():
    clear_screen()
    print("What would you like to do?")
    print("1. Add New Team Member")
    print("2. Assign Individual to Manager")
    print("3. Search for an Individual")
    print("4. Management Printout")
    print("")
    print("0. Exit")
    choice = "X"

    while choice not in ("1234"):
        choice = input("Selection: ")
    
    if choice == "1":
        add_member()
    elif choice == "2":
        assign()
    elif choice == "3":
        search()
    elif choice == "4":
        printout()
    elif choice == "0":
        exit(0)
    else:
        print("Unknown error occurred!")

def print_header(header_text):
    print("")
    print('*' * len(header_text))
    print(header_text)
    print('-' * len(header_text))

def add_member():
    global person_id_index 
    global persons
    print_header("Add New Person")
    first = input("First Name: ")
    last = input("Last Name: ")
    position = input("Position/Title: ")
    
    p = Person(first, last, position, person_id_index)
    persons[person_id_index] = p
    person_id_index += 1
    print(f"Successfully added {p.get_short_description()}")
    wait_enter()
    menu_display()

def search():
    global persons
    print_header("Search")
    search_id = int(input("Enter the ID: "))
    result = persons.get(search_id)
    
    if result != None:
        result.display_card()
    else:
        print("Person not found.")

    wait_enter()
    menu_display()


def printout():
    pass

def assign():
    pass

# Start Here
menu_display()