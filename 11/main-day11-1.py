import time
from collections import deque


def read_input_file():
    with open("./input1.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_grid(lines):
    grid = []
    for line in lines:
        # Remove newline characters and convert the line into a list of characters
        row = list(line.strip())
        grid.append(row)
    return grid


def double_empty_rows_and_columns(grid):
    # Double rows without '#'
    doubled_grid = []
    for row in grid:
        if '#' not in row:
            doubled_grid.extend([row, row.copy()])
        else:
            doubled_grid.append(row)

    # Double columns without '#'
    transposed_grid = list(zip(*doubled_grid))
    doubled_transposed = []
    for column in transposed_grid:
        if '#' not in column:
            doubled_transposed.extend([column, column])
        else:
            doubled_transposed.append(column)

    # Transpose back to original form
    return [list(row) for row in zip(*doubled_transposed)]


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


def bfs(grid, start, goal):
    visited = set()
    queue = deque([(start, 0)])  # (position, distance)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, right, down, left

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == goal:
            return dist
        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != '#':
                    queue.append(((nx, ny), dist + 1))

    return float('inf')  # If no path found


def calculate_paths_sum(grid, galaxies):
    path_lengths = []
    galaxy_numbers = sorted(galaxies.keys())
    total_galaxies = len(galaxy_numbers)
    total_pairs = total_galaxies * (total_galaxies - 1) / 2
    completed_pairs = 0
    total_time_spent = 0

    for i in range(total_galaxies):
        start_time = time.time()  # Start time for this galaxy's pairs

        for j in range(i + 1, total_galaxies):
            path_length = bfs(grid, galaxies[galaxy_numbers[i]], galaxies[galaxy_numbers[j]])
            path_lengths.append(path_length)
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
doubled_grid = double_empty_rows_and_columns(grid)
numbered_galaxy = number_galaxies(doubled_grid)
galaxies = find_galaxies(numbered_galaxy)
total_path_length = calculate_paths_sum(doubled_grid, galaxies)

print("Sum of shortest paths between all galaxy pairs:", total_path_length)
