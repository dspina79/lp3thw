import mymodule

print("Now we are going to output data from a module.")
print(f"{mymodule.module_variable}")
print("Now calling a function.")
name = "Dean"
print(f"This is the output: {mymodule.greet(name)}.")
