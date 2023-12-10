import sys
sys.setrecursionlimit(20000)  # Set a new limit, e.g., 1500 or 2000


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


def find_starting_position(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                return (x, y)
    return None


def valid_connection(grid, x, y, x_next, y_next):
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and 0 <= y_next < len(grid) and 0 <= x_next < len(grid[0]):
        current_cell = grid[y][x]
        next_cell = grid[y_next][x_next]

        if current_cell == '|':
            if next_cell == '|' and (y_next == y - 1 or y_next == y + 1):
                return True
            if next_cell == 'L' and y_next == y + 1:
                return True
            if next_cell == 'J' and y_next == y + 1:
                return True
            if next_cell == '7' and y_next == y - 1:
                return True
            if next_cell == 'F' and y_next == y - 1:
                return True

        if current_cell == '-':
            if next_cell == '-' and (x_next == x - 1 or x_next == x + 1):
                return True
            if next_cell == '7' and x_next == x + 1:
                return True
            if next_cell == 'F' and x_next == x - 1:
                return True
            if next_cell == 'J' and x_next == x + 1:
                return True
            if next_cell == 'L' and x_next == x - 1:
                return True

        if current_cell == 'L':
            if next_cell == '|' and y_next == y - 1:
                return True
            if next_cell == '-' and x_next == x + 1:
                return True
            if next_cell == 'J' and x_next == x + 1:
                return True
            if next_cell == '7' and x_next == x + 1:
                return True
            if next_cell == '7' and y_next == y - 1:
                return True
            if next_cell == 'F' and y_next == y - 1:
                return True

        if current_cell == 'J':
            if next_cell == '|' and y_next == y - 1:
                return True
            if next_cell == '-' and x_next == x - 1:
                return True
            if next_cell == 'F' and y_next == y - 1:
                return True
            if next_cell == 'F' and x_next == x - 1:
                return True
            if next_cell == '7' and y_next == y - 1:
                return True
            if next_cell == 'L' and x_next == x - 1:
                return True

        if current_cell == '7':
            if next_cell == '|' and y_next == y + 1:
                return True
            if next_cell == '-' and x_next == x - 1:
                return True
            if next_cell == 'L' and x_next == x - 1:
                return True
            if next_cell == 'L' and y_next == y + 1:
                return True
            if next_cell == 'F' and x_next == x - 1:
                return True
            if next_cell == 'J' and y_next == y + 1:
                return True

        if current_cell == 'F':
            if next_cell == '|' and y_next == y + 1:
                return True
            if next_cell == '-' and x_next == x + 1:
                return True
            if next_cell == 'J' and y_next == y + 1:
                return True
            if next_cell == 'J' and x_next == x + 1:
                return True
            if next_cell == 'L' and y_next == y + 1:
                return True
            if next_cell == '7' and x_next == x + 1:
                return True

        if current_cell == 'S':
            return next_cell in ['|', '-', 'L', 'J', '7', 'F']

    return False


# Initialize maximum distance info with distance 0 and empty path
max_distance_info = {"distance": 0, "path": []}


def navigate_with_path(grid, x, y, visited, path, max_distance_info, current_distance=0):
    if (x, y) in visited:
        return max_distance_info

    visited.add((x, y))
    new_path = path + [(x, y)]  # Append the current position to the path

    # Update the maximum distance and path if the current distance is greater
    if current_distance > max_distance_info["distance"]:
        max_distance_info = {"distance": current_distance, "path": list(new_path)}

    # Check all four directions
    if valid_connection(grid, x, y, x, y - 1):  # North
        max_distance_info = navigate_with_path(grid, x, y - 1, visited, new_path, max_distance_info, current_distance + 1)
    if valid_connection(grid, x, y, x, y + 1):  # South
        max_distance_info = navigate_with_path(grid, x, y + 1, visited, new_path, max_distance_info, current_distance + 1)
    if valid_connection(grid, x, y, x + 1, y):  # East
        max_distance_info = navigate_with_path(grid, x + 1, y, visited, new_path, max_distance_info, current_distance + 1)
    if valid_connection(grid, x, y, x - 1, y):  # West
        max_distance_info = navigate_with_path(grid, x - 1, y, visited, new_path, max_distance_info, current_distance + 1)

    visited.remove((x, y))  # Remove the current position as we backtrack
    return max_distance_info


def visualize_path(grid, path):
    # Create a copy of the grid to modify
    grid_with_path = [row[:] for row in grid]

    number = 0

    # Mark the path on the grid
    for x, y in path:
        grid_with_path[y][x] = '*'
        number += 1

    # Create a string representation of the grid
    visualized_grid = "\n".join(["".join(row) for row in grid_with_path])
    return visualized_grid


lines = read_input_file()
grid = parse_grid(lines)
starting_position = find_starting_position(grid)
print(f"The starting position is: {starting_position}")
farthest_info = navigate_with_path(grid, starting_position[0], starting_position[1], set(), [], max_distance_info, 0)
print(f"The farthest distance is: {(farthest_info['distance'] + 1) / 2}")
