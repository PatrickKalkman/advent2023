def read_input_file():
    with open("./input1.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_grid(lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid


def simulate_beam_with_optimized_splitting(grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    beams = {((0, 0), 0)}  # Initial beam position and direction (right)
    energized_tiles = set()
    processed = set()  # To track already processed beams

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

    return len(energized_tiles)


lines = read_input_file()
grid = parse_grid(lines)
energized_count_with_optimized_splitting = simulate_beam_with_optimized_splitting(grid)
print(energized_count_with_optimized_splitting)
