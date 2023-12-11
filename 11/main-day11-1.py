def read_input_file():
    with open("./test-input1.txt", "r") as open_file:
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


def print_grid(grid):
    for row in grid:
        print(' '.join(row))


lines = read_input_file()
grid = parse_grid(lines)
doubled_grid = double_empty_rows_and_columns(grid)
print_grid(grid)
print(len(grid), len(grid[0]))
print_grid(doubled_grid)
print(len(doubled_grid), len(doubled_grid[0]))
