# Conditionals with Else If

people = 50
cars = 20
trucks = 40

# test if there are enough cars for people
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

# test if there are more cars available than trucks
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

# if there are more people than trucks then indicate we can use the trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

