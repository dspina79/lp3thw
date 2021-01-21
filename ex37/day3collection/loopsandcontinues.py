# While Loops with Continues

def output_cubes_not_divisible_by_3(upper_range):
    starter = 1
    while starter < upper_range:
        cube = starter ** 3
        starter += 1
        if cube % 3 == 0:
            continue
        print(cube)


output_cubes_not_divisible_by_3(100)