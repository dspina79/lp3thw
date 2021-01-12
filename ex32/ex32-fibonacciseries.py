# Try the Fibonocci Series

def base_fib(to_range):
    series = [1,1]

    for i in range(0, to_range):
        next_num = series[-1] + series[-2]
        series.append(next_num)
    return series

def extend_level_1(series):
    start = 0
    num1 = series[start]
    num2 = series[start + 1]
    while start < len(series) - 1:
        diff = num2 - num1
        series.insert(start + 1, diff)
        start += 2
        try:
            num1 = series[start]
            num2 = series[start + 1]
        except:
            start = len(series)

    return series

def extend_levels(series, instances):
    for i in (0, instances):
        series = extend_level_1(series)
    return series

def extended_levels_to_file(series, instances):
    extended_series = extend_levels(series, instances)
    extfile = open("series.txt", "w")
    for i in extended_series:
        extfile.write(f"{i}\n")
    
    extfile.close()

range_limit = int(input("How far out? "))

fib_series = base_fib(range_limit)
print(fib_series)
level_1_extrapolation = extend_level_1(fib_series)
print(level_1_extrapolation)

instances = int(input("How many times do you want to run it?"))
extended_series = extend_levels(fib_series, instances)
print(extended_series)
extended_levels_to_file(fib_series, instances)
