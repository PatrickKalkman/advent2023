import re


def read_input_file():
    with open("input1.txt", "r") as open_file:
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


def determine_all_possible_games(games, cube_bag):

    possible_games = []
    for game_id, cube_sets in games.items():
        game_possible = True
        for cube_set in cube_sets:
            for color, amount in cube_set.items():
                if amount > cube_bag[color]:
                    game_possible = False
                    break

            if not game_possible:
                break

        if game_possible:
            possible_games.append(int(game_id))

    return possible_games


bag = {'red': 12, 'green': 13, 'blue': 14}
lines = read_input_file()
games = parse_lines(lines)
possible_games = determine_all_possible_games(games, bag)
print(possible_games)
# add all numbers in possible_games
print(sum(possible_games))

