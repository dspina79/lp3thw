# Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are now {len(stuff)} items in the list.")

print("There we go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # goes backwards
print(stuff.pop())
print(' '.join(stuff)) # displays a string
print('#'.join(stuff[3:5]))

# some other list functions
print("Reverse()")
stuff.reverse()
print(stuff)
# put it back to normal
print("Put the things back in order")
stuff.reverse()
print(stuff)

print("Inserting a kiwi")
print(f"Before insertion: {stuff}")
stuff.insert(3, "kiwi")
print(f"After insertion at 3: {stuff}")
print("That puts it as the FOURTH item in the list.")
