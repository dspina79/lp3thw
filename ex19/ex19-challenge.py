# Exercise 19 Challenge

def babylonianSquareRoot(num):
    x = num
    y = 1
    e = 0.0000001

    while x - y > e:
        x = (x + y) / 2
        y = num / x
    return x

print("According to the Babylonians...")

print(f"The square root of 4 is {babylonianSquareRoot(4)}")
my_num = 49
my_num_root = babylonianSquareRoot(my_num)
print(f"The square root of {my_num} is {my_num_root}")

my_num = 64
my_num_root = babylonianSquareRoot(my_num)
print(f"The square root of {my_num} is {my_num_root}")

my_num = 256
my_num_root = babylonianSquareRoot(my_num)
print(f"The square root of {my_num} is {my_num_root}")


my_arr = [1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,50]
for x in my_arr:
    print(f"The square root of {x} is {babylonianSquareRoot(x)}")


x_var = int(input("Get the square root of: "))
print(f"The square root of {x_var} is {babylonianSquareRoot(x_var)}.")