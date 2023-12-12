import time
from collections import deque


def read_input_file():
    with open("./input2.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_grid(lines):
    grid = []
    for line in lines:
        # Remove newline characters and convert the line into a list of characters
        row = list(line.strip())
        grid.append(row)
    return grid


def number_galaxies(grid):
    galaxy_number = 1
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] == '#':
                grid[y][x] = str(galaxy_number)
                galaxy_number += 1
    return grid


def find_galaxies(grid):
    galaxies = {}
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val.isdigit():
                galaxies[int(val)] = (x, y)
    return galaxies


def adjust_coordinates(galaxies, grid):
    # Check for empty rows (no galaxy number)
    row_expansion = [1000000 if not any(val.isdigit() for val in row) else 1 for row in grid]

    # Check for empty columns (no galaxy number)
    transposed_grid = zip(*grid)
    column_expansion = [1000000 if not any(val.isdigit() for val in column) else 1 for column in transposed_grid]

    adjusted_galaxies = {}
    for galaxy, (x, y) in galaxies.items():
        # Adjust the x-coordinate
        adjusted_x = x
        for i in range(x):
            if column_expansion[i] == 1000000:
                adjusted_x += (1000000 - 1)  # Add 1 for each expanded column before the galaxy

        # Adjust the y-coordinate
        adjusted_y = y
        for i in range(y):
            if row_expansion[i] == 1000000:
                adjusted_y += (1000000 - 1)  # Add 1 for each expanded row before the galaxy

        adjusted_galaxies[galaxy] = (adjusted_x, adjusted_y)

    return adjusted_galaxies




def calculate_adjusted_paths_sum(adjusted_galaxies):
    path_lengths = []
    galaxy_numbers = sorted(adjusted_galaxies.keys())

    for i in range(len(galaxy_numbers)):
        for j in range(i + 1, len(galaxy_numbers)):
            x1, y1 = adjusted_galaxies[galaxy_numbers[i]]
            x2, y2 = adjusted_galaxies[galaxy_numbers[j]]
            distance = abs(x1 - x2) + abs(y1 - y2)
            path_lengths.append(distance)

    return sum(path_lengths)


def print_grid(grid):
    for row in grid:
        print(''.join(row))


# Main execution
lines = read_input_file()
grid = parse_grid(lines)
numbered_galaxy = number_galaxies(grid)
galaxies = find_galaxies(numbered_galaxy)
adjusted_galaxies = adjust_coordinates(galaxies, grid)
total_path_length = calculate_adjusted_paths_sum(adjusted_galaxies)
print("Sum of shortest paths between all galaxy pairs:", total_path_length)