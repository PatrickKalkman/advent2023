from functools import reduce


def read_input_file():
    with open("input2.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def calculate_distance(time_held, total_duration):
    speed = time_held
    time_moving = total_duration - time_held
    distance = speed * time_moving
    return distance


def parse_race_info(lines):
    race_times = []
    record_distances = []

    if lines and len(lines) > 0:
        race_times = [int(time.strip()) for time in lines[0].split()[1:]]

    if len(lines) > 1:
        record_distances = [int(distance.strip()) for distance in lines[1].split()[1:]]

    race_info = list(zip(race_times, record_distances))
    return race_info


def simulate_races(race_info):
    possible_wins = []
    for (total_duration, record_distance) in race_info:
        possible_win = 0
        for time_held in range(total_duration + 1):
            distance = calculate_distance(time_held, total_duration)
            # print(f"Holding the button for {time_held} ms results in the boat traveling {distance} mm.")
            if (distance > record_distance):
                possible_win += 1
        possible_wins.append(possible_win)
    return possible_wins


def multiply_list_elements(my_list):
    return reduce(lambda x, y: x * y, my_list)


lines = read_input_file()
race_info = parse_race_info(lines)
possible_wins = simulate_races(race_info)
total = multiply_list_elements(possible_wins)

print(total)
