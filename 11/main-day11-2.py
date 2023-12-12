import time
from collections import deque


def read_input_file():
    with open("./test-input2.txt", "r") as open_file:
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


def original_distances(galaxies):
    distances = {}
    for i, (key1, (x1, y1)) in enumerate(galaxies.items()):
        for key2, (x2, y2) in list(galaxies.items())[i+1:]:
            distance = abs(x1 - x2) + abs(y1 - y2)
            distances[(key1, key2)] = distance
    return distances


def expand_distances(distances, row_multiplier, column_multiplier):
    expanded_distances = {}
    for (galaxy1, galaxy2), distance in distances.items():
        row_distance = sum(row_multiplier[min(galaxies[galaxy1][1], galaxies[galaxy2][1]):max(galaxies[galaxy1][1], galaxies[galaxy2][1])])
        column_distance = sum(column_multiplier[min(galaxies[galaxy1][0], galaxies[galaxy2][0]):max(galaxies[galaxy1][0], galaxies[galaxy2][0])])
        expanded_distances[(galaxy1, galaxy2)] = row_distance + column_distance
    return expanded_distances


def expand_multiplier(grid):
    row_multiplier = [10 if '#' not in row else 1 for row in grid]
    column_multiplier = [10 if '#' not in column else 1 for column in zip(*grid)]
    return row_multiplier, column_multiplier


def adjust_galaxy_coordinates(galaxies, row_multiplier, column_multiplier):
    adjusted_galaxies = {}
    for number, (x, y) in galaxies.items():
        adjusted_x = x
        adjusted_y = y

        for i in range(y):
            adjusted_y += (row_multiplier[i] - 1)
        for i in range(x):
            adjusted_x += (column_multiplier[i] - 1)

        adjusted_galaxies[number] = (adjusted_x, adjusted_y)
    return adjusted_galaxies


def calculate_manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def calculate_paths_sum(galaxies):
    path_lengths = []
    galaxy_numbers = sorted(galaxies.keys())
    total_galaxies = len(galaxy_numbers)
    total_pairs = total_galaxies * (total_galaxies - 1) / 2
    completed_pairs = 0
    total_time_spent = 0

    for i in range(total_galaxies):
        start_time = time.time()  # Start time for this galaxy's pairs

        for j in range(i + 1, total_galaxies):
            distance = calculate_manhattan_distance(galaxies[galaxy_numbers[i]], galaxies[galaxy_numbers[j]])
            path_lengths.append(distance)
            completed_pairs += 1

        end_time = time.time()  # End time for this galaxy's pairs
        time_taken = end_time - start_time
        total_time_spent += time_taken

        # Average time per pair
        avg_time_per_pair = total_time_spent / completed_pairs
        # Estimate time remaining for all pairs
        estimated_time_remaining = avg_time_per_pair * (total_pairs - completed_pairs)

        print(f"Completed pairs with galaxy {i + 1}/{total_galaxies}. Estimated time remaining: {estimated_time_remaining:.2f} seconds")

    return sum(path_lengths)


def print_grid(grid):
    for row in grid:
        print(' '.join(row))


# Main execution
lines = read_input_file()
grid = parse_grid(lines)
numbered_galaxy = number_galaxies(grid)
galaxies = find_galaxies(numbered_galaxy)

row_multiplier, column_multiplier = expand_multiplier(grid)
original_dist = original_distances(galaxies)
expanded_dist = expand_distances(original_dist, row_multiplier, column_multiplier)

total_path_length = sum(expanded_dist.values())
print("Sum of shortest paths between all galaxy pairs:", total_path_length)