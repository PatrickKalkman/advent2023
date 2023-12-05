
def read_input_file():
    with open("input1.txt", "r") as open_file:
        lines = open_file.readlines()

    return lines


def parse_lines(lines):
    return [list(row.strip()) for row in lines]


def is_symbol(char):
    return not char.isnumeric() and char != '.'


def check_adjacent(grid, x_start, y, length):
    adjacent_offsets = [
        (-1, -1), (-1, 0), (-1, 1),  # Above
        (0, -1),           (0, 1),   # Sides
        (1, -1),  (1, 0),  (1, 1)    # Below
    ]
    for i in range(length):
        x = x_start + i
        for dx, dy in adjacent_offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if is_symbol(grid[ny][nx]):
                    return True
    return False


def traverse_grid(grid):
    total = 0
    for y in range(len(grid)):
        number = ''
        for x in range(len(grid[y])):
            char = grid[y][x]
            if char.isnumeric():
                number += char
                # Check for symbols adjacent to the last digit of the number
                if x == len(grid[y]) - 1 or not grid[y][x + 1].isnumeric():
                    if check_adjacent(grid, x - len(number) + 1, y, len(number)):
                        total += int(number)
                        print(f"Adding {number} at ({y}, {x - len(number) + 1})")
                    number = ''
            else:
                if number:
                    # Check for symbols adjacent to the first digit of the number
                    if check_adjacent(grid, x - len(number), y, len(number)):
                        total += int(number)
                        print(f"Adding {number} at ({y}, {x - len(number)})")
                    number = ''
    return total


lines = read_input_file()
grid = parse_lines(lines)
total = traverse_grid(grid)
print(total)
