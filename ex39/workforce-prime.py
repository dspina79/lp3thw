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
    def __init__(self, manager_id, worker_id, relationship_notes):
        super().__init__()
        self.worker = worker_id
        self.manager = manager_id
        self.notes = relationship_notes


def clear_screen():
    """Clears the terminal screen of content"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def wait_enter():
    """Waits for the user to hit enter before continuing."""
    print("")
    val = input("Press ENTER to continue.")

def menu_display():
    """Initial state of the application. Provides menu options."""
    clear_screen()
    print("")
    print("What would you like to do?")
    print("1. Add New Team Member")
    print("2. Assign Individual to Manager")
    print("3. Search for an Individual")
    print("4. Management Printout")
    print("5. Management Writeout")
    print("")
    print("0. Exit")
    choice = "X"

    while choice not in ("12345"):
        choice = input("Selection: ")
    
    if choice == "1":
        add_member()
    elif choice == "2":
        assign()
    elif choice == "3":
        search()
    elif choice == "4":
        printout()
    elif choice == "5":
        writeout("managers.txt")
    elif choice == "0":
        exit(0)
    else:
        print("Unknown error occurred!")

def print_header(header_text):
    """Outputs a header, formatted."""
    print("")
    print('*' * len(header_text))
    print(header_text)
    print('-' * len(header_text))

def add_member():
    """Adds an employee to the internal collection"""
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
    """Searches for an individual based on a supplied ID"""
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

def writeout(filename):
    """Outputs the managerial information and hierarchy into a file"""
    f = open(filename, 'w')
    for manager_id, worker_assignments in list(manager_assignments.items()):
        manager = persons.get(manager_id)
        f.write(f"Manager: {manager.get_short_description()}")
        for assignment in worker_assignments:
            worker = persons.get(assignment.worker)
            f.write(f"\n\tWorker: {worker.get_short_description()}")
        print("\n")
    f.close()

    print(f"Successfully wrote to the file {filename}")
    wait_enter()
    menu_display()

def printout():
    for manager_id, worker_assignments in list(manager_assignments.items()):
        manager = persons.get(manager_id)
        print(f"Manager: {manager.get_short_description()}")
        for assignment in worker_assignments:
            worker = persons.get(assignment.worker)
            print(f"\tWorker: {worker.get_short_description()}")

    wait_enter()
    menu_display()

def assign():
    print_header("Assign to Manager")
    manager_id = int(input("Enter the manager ID: "))
    if persons.get(manager_id) == None:
        print("Manager with that id is not found.")
        return
    
    worker_id = int(input("Enter the employee's ID: "))
    if persons.get(worker_id) == None:
        print("Manager with that id is not found.")
        return
    
    notes = input("Provide any notes: ")

    entry = ManagerAssignment(manager_id, worker_id, notes)
    
    if manager_assignments.get(manager_id) == None:
        manager_assignments[manager_id] = []
    
    worker_listing = manager_assignments.get(manager_id)
    worker_listing.append(entry)
    manager_assignments[manager_id] = worker_listing
    print("Successfully updating listing.")
    wait_enter()
    menu_display()

# Start Here
menu_display()