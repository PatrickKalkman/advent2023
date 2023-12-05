
def read_input_file():
    with open("input2.txt", "r") as open_file:
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
                if grid[ny][nx] == '*':
                    return (nx, ny)
    return None


def find_number_pairs(grid):
    star_adjacent = {}  # Dictionary to store numbers adjacent to each '*'

    for y in range(len(grid)):
        number = ''
        for x in range(len(grid[y])):
            char = grid[y][x]
            if char.isnumeric():
                number += char
                if x == len(grid[y]) - 1 or not grid[y][x + 1].isnumeric():
                    star_pos = check_adjacent(grid, x - len(number) + 1, y, len(number))
                    if star_pos:
                        star_adjacent.setdefault(star_pos, []).append(int(number))
                    number = ''
            else:
                if number:
                    star_pos = check_adjacent(grid, x - len(number), y, len(number))
                    if star_pos:
                        star_adjacent.setdefault(star_pos, []).append(int(number))
                    number = ''

    return star_adjacent


lines = read_input_file()
grid = parse_lines(lines)
number_pairs = find_number_pairs(grid)

total = 0
for star_pos, numbers in number_pairs.items():
    if len(numbers) > 1:
        print(f"Star at {star_pos} is adjacent to number pairs: {numbers}")
        total += numbers[0] * numbers[1]

print(total)