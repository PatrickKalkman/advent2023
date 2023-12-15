import itertools
import concurrent.futures
import os


def read_input_file():
    with open("./test-input2.txt", "r") as open_file:
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


def unfold_row(springs, error):
    unfolded_springs = '?'.join(''.join(springs) for _ in range(5))
    unfolded_error = ','.join(','.join(str(e) for e in error) for _ in range(5))
    return unfolded_springs, unfolded_error


def process_spring_row(spring_row):
    springs, error = spring_row
    unfolded_springs, unfolded_error = unfold_row(springs, error)
    error_list = [int(e) for e in unfolded_error.split(',')]
    arrangements = brute_force_arrangements(list(unfolded_springs), error_list)
    return unfolded_springs, unfolded_error, arrangements


def main():
    lines = read_input_file()
    spring_info = parse_spring_info(lines)

    total_arrangements = 0
    num_workers = os.cpu_count()  # You can set this to a specific number if needed
    print("Number of workers:", num_workers)

    with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
        results = executor.map(process_spring_row, spring_info)
        for unfolded_springs, unfolded_error, arrangements in results:
            total_arrangements += arrangements
            print("Unfolded Row:", unfolded_springs, "Error:", unfolded_error, "Arrangements:", arrangements)

    print("Total arrangements for all lines:", total_arrangements)

if __name__ == "__main__":
    main()