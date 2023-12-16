def read_input_file():
    with open("./input1.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_blocks(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid


def process_north(grid):
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    # Keep track if any 'O' moved in the current iteration
    moved = True
    while moved:
        moved = False
        for col in range(num_cols):
            # Start from the second row (first row can't move up)
            for row in range(1, num_rows):
                if grid[row][col] == 'O' and grid[row - 1][col] == '.':
                    # Swap 'O' with '.'
                    grid[row][col], grid[row - 1][col] = grid[row - 1][col], grid[row][col]
                    moved = True


def print_grid(grid):
    for row in grid:
        print("".join(row))


def calculate_load(grid):
    num_rows = len(grid)
    total_load = 0
    for row in range(num_rows):
        for cell in grid[row]:
            if cell == 'O':
                # Load is the row number from the bottom
                load = num_rows - row
                total_load += load
    return total_load


lines = read_input_file()
grid = parse_blocks(lines)
process_north(grid)
total_load = calculate_load(grid)
print("Total load:", total_load)
