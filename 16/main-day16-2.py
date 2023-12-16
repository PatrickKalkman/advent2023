def read_input_file():
    with open("./input2.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_grid(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid


def simulate_beam_from_start(grid, start_x, start_y, start_direction):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    beams = {((start_x, start_y), start_direction)}
    energized_tiles = set()
    processed = set()

    while beams:
        new_beams = set()
        for (x, y), direction in beams:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and ((x, y), direction) not in processed:
                tile = grid[x][y]
                energized_tiles.add((x, y))
                processed.add(((x, y), direction))

                if tile in ['/', '\\']:
                    direction = 3 - direction if tile == '/' else (1 - direction) % 4
                elif tile in ['|', '-']:
                    # Handle beam splitting
                    if (direction % 2 == 0 and tile == '|'):
                        new_beams.add(((x, y), 1))  # Split beam going down
                        new_beams.add(((x, y), 3))  # Split beam going up
                        continue
                    elif (direction % 2 == 1 and tile == '-'):
                        new_beams.add(((x, y), 0))  # Split beam going right
                        new_beams.add(((x, y), 2))  # Split beam going left
                        continue

                # Move the beam
                dx, dy = directions[direction]
                new_beams.add(((x + dx, y + dy), direction))

        beams = new_beams

    return energized_tiles


def find_correct_max_energized_configuration(grid):
    max_energized_count = 0
    best_start_position = None
    best_start_direction = None

    rows, cols = len(grid), len(grid[0])

    # Top and Bottom rows, beam moving Down and Up respectively
    for y in range(cols):
        # Top row, beam moving Down
        energized_count = len(simulate_beam_from_start(grid, 0, y, 1))
        if energized_count > max_energized_count:
            max_energized_count = energized_count
            best_start_position = (0, y)
            best_start_direction = 1

        # Bottom row, beam moving Up
        energized_count = len(simulate_beam_from_start(grid, rows - 1, y, 3))
        if energized_count > max_energized_count:
            max_energized_count = energized_count
            best_start_position = (rows - 1, y)
            best_start_direction = 3

    # Left and Right columns, beam moving Right and Left respectively
    for x in range(rows):
        # Left column, beam moving Right
        energized_count = len(simulate_beam_from_start(grid, x, 0, 0))
        if energized_count > max_energized_count:
            max_energized_count = energized_count
            best_start_position = (x, 0)
            best_start_direction = 0

        # Right column, beam moving Left
        energized_count = len(simulate_beam_from_start(grid, x, cols - 1, 2))
        if energized_count > max_energized_count:
            max_energized_count = energized_count
            best_start_position = (x, cols - 1)
            best_start_direction = 2

    return max_energized_count, best_start_position, best_start_direction


lines = read_input_file()
grid = parse_grid(lines)
max_count, start_position, start_direction = find_correct_max_energized_configuration(grid)
print(max_count, start_position, start_direction)
