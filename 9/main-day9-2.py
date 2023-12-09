def read_input_file():
    with open("input2.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_lines(lines):
    number_lines = []
    for line in lines:
        numbers = line.strip().split()
        numbers = [int(number) for number in numbers]
        number_lines.append(numbers)
    return number_lines


def calculate_history(number_line):
    history = [number_line] 

    while True:
        current_sequence = history[-1]
        next_sequence = [current_sequence[i + 1] - current_sequence[i] for i in range(len(current_sequence) - 1)]

        history.append(next_sequence)

        # Check if all elements in the next sequence are zero
        if all(x == 0 for x in next_sequence):
            break

    return history


def calculate_all_history(number_lines):
    histories = []
    for line in number_lines:
        history = calculate_history(line)
        histories.append(history)
    return histories


def extrapolate_previous_value(history):
    history[-1].insert(0, 0)

    for i in range(len(history) - 2, -1, -1):
        new_value = history[i][0] - history[i + 1][0]
        history[i].insert(0, new_value)

    return history[0][0]


lines = read_input_file()
number_lines = parse_lines(lines)
histories = calculate_all_history(number_lines)

total = 0
for history in histories:
    next_value = extrapolate_previous_value(history)
    total += next_value
    print(f"The next value in the sequence is: {next_value}")
    print("Visual representation of the sequences:")
    for sequence in history:
        print("   " * (len(history) - len(sequence)), "   ".join(map(str, sequence)))

print(f"The sum of all next values is: {total}")
