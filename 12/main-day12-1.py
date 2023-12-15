import itertools


def read_input_file():
    with open("./input1.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_spring_info(lines):
    spring_info = []
    for line in lines:
        parts = line.strip().split(" ")
        springs = list(parts[0])
        error = [int(num) for num in parts[1].split(",")]
        spring_info.append((springs, error))
    return spring_info


def is_valid(row, error):
    i = 0
    for group_size in error:
        while i < len(row) and row[i] != '#':
            i += 1
        count = 0
        while i < len(row) and row[i] == '#':
            count += 1
            i += 1
        if count != group_size:
            return False
    return all(s != '#' for s in row[i:])


def brute_force_arrangements(springs, error):
    unknown_count = springs.count('?')
    valid_arrangements = 0

    for combination in itertools.product(['.', '#'], repeat=unknown_count):
        temp_row = springs[:]
        comb_index = 0

        for i in range(len(temp_row)):
            if temp_row[i] == '?':
                temp_row[i] = combination[comb_index]
                comb_index += 1

        if is_valid(temp_row, error):
            valid_arrangements += 1

    return valid_arrangements


# Main execution
lines = read_input_file()
spring_info = parse_spring_info(lines)

total_arrangements = 0
for springs, error in spring_info:
    arrangements = brute_force_arrangements(springs, error)
    total_arrangements += arrangements
    print("Row:", ''.join(springs), "Error:", error, "Arrangements:", arrangements)

print("Total arrangements for all lines:", total_arrangements)
