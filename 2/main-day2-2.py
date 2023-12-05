import re


def read_input_file():
    with open("input2.txt", "r") as open_file:
        lines = open_file.readlines()

    return lines


def parse_lines(lines):

    games = {}
    for line in lines:
        # Extracting the game identifier and the sets of cube picks
        match = re.match(r"Game (\d+): (.+)", line)
        if match:
            game_id = match.group(1)
            sets = match.group(2).split(';')

            # Parsing each set to extract the number and color of cubes
            cube_sets = []
            for set_ in sets:
                cubes = re.findall(r'(\d+) (\w+)', set_)
                cube_sets.append({color: int(number) for number, color in cubes})

            games[game_id] = cube_sets

    return games


def determine_game_power(games):

    powers = []
    for game_id, cube_sets in games.items():
        color_amount = {}
        for cube_set in cube_sets:
            for color, amount in cube_set.items():
                if color in color_amount:
                    if amount > color_amount[color]:
                        color_amount[color] = amount
                else:
                    color_amount[color] = amount
        # calculate the power of the game by multiplying the values in the color_amount dict
        power = 1
        for value in color_amount.values():
            power *= value
        powers.append(power)

    return powers


lines = read_input_file()
games = parse_lines(lines)
game_power = determine_game_power(games)
total = sum(game_power)
print(total)
