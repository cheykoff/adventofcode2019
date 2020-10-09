"""
Problem:
Calculate the fuel based on the masses of modules

Input:
txt file with masses (whole numbers)
formula: fuel = sum over all modules (round_down (mass of the module / 3) - 2)

Output:
amount of fuel

Approach 1:
Read txt file
Store each line (one number) as an integer in a list
Calculate the fuel for each module (seperate function)
Sum all fuels 
Print sum

Approach 2:
Use Generator to read each line (one module mass) 
Calculate the fuel for the  module
Add it to the total fuel needed
Print total fuel

Approach 3:
Read txt file
Store each line (one number) as an integer in a list
Use List comprehension to calculate a list of fuels
Sum all fuels
Print 

Approach 4:
Read the lines in batches (combine 2 & 3)

Design tradeoffs (best to worst, expected)
time to implement: 1, 3, 2
memory: 2, 3, 1
performance (small data): 3, 1, 2
performance (big data): 2, 3, 1
readability: ?

Potential add-ons:
check if each input is valid (typeof(int))
performance and memory optimization
"""

from sys import stdin


def calculate_fuel_from_mass(mass):
    # Floor division will round positive numbers down to whole integers
    fuel = (mass // 3) - 2
    return fuel


def read_file_1():
    with open("data/day_01.txt") as file:
        masses = []
        for line in file:
            masses.append(int(line))

        print(masses)


def read_file_2():
    with open("data/day_01.txt") as file:
        lines = file.readlines()
        masses = [int(line) for line in lines]
        print(masses)


def read_file_3():
    # use generator
    with open("data/day_01.txt") as file:
        lines = file.readlines()
        for line in lines:
            yield line


def read_file_4():
    # treat file descriptor as generator (file remains open)
    return open("data/day_01.txt")


def read_file_5():
    # use stdin
    return stdin
    # cat data/day_01.txt | python day_01.py (unix)
    # type data\day_01.txt | python day_01.py (windows)


def calculate_fuel():
    temp = map(int, read_file_3())
    temp2 = map(calculate_fuel, temp)
    print(sum(temp2))


if __name__ == "__main__":
    """
    mass = 14
    modules = [12, 14, 1969, 100756]
    total_fuel = 0

    for module in modules:
        fuel = calculate_fuel(module)
        total_fuel += fuel

    print(type(total_fuel))
    print(total_fuel)

    read_file_1()
    read_file_2()
    # print(sum(calculate_fuel(int(read_file_3()))))
    temp = map(int, read_file_3())
    temp2 = map(calculate_fuel, temp)
    print(sum(temp2))
    """

    temp = map(int, read_file_3())
    temp2 = map(calculate_fuel, temp)
    print(sum(temp2))
