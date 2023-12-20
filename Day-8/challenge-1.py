import math

def number_of_cans_needed(height, width, coverage):
    area = height * width
    number_of_cans = math.ceil(area / coverage)
    print(f"The number of cans needed is: {number_of_cans}")

height = int(input("Height of the wall is: "))
width = int(input("Width of the wall is: "))
covered_space = 5

number_of_cans_needed(height, width, covered_space)