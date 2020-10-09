def calculate_fuel_from_mass(mass):
    # Floor division will round positive numbers down to whole integers
    fuel = (mass // 3) - 2
    return fuel


def read_file():
    # use generator
    with open("data/day_01.txt") as file:
        lines = file.readlines()
        for line in lines:
            yield line


def calculate_fuel(lines):
    return sum(map(calculate_fuel_from_mass, map(int, lines)))


if __name__ == "__main__":
    print(calculate_fuel(read_file()))
