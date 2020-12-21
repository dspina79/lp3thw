# Printing, Printing, Printing

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "There once was a princess from Boston",
    "Who couldn't find a coat or a button",
    "When she looked all around, and then she found",
    "Her clothes were made out of cotton"
))

# try with an incorrect number of arguments
#print(formatter.format(1,2,3)) Fails
print(formatter.format(1,2,3,4,5)) #prints 1-4, not 5