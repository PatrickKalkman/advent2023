def read_input_file():
    with open("input1.txt", "r") as open_file:
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
    history = [number_line]  # Initialize history with the input sequence

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


def extrapolate_next_value(history):
    # Extend the last row with a zero
    history[-1].append(0)

    # Work upwards through the history
    for i in range(len(history) - 2, -1, -1):
        new_value = history[i][-1] + history[i + 1][-1]  # Change here
        history[i].append(new_value)

    # The last value in the first row is the next value in the sequence
    return history[0][-1]


lines = read_input_file()
number_lines = parse_lines(lines)
histories = calculate_all_history(number_lines)

total = 0
for history in histories:
    next_value = extrapolate_next_value(history)
    total += next_value
    print(f"The next value in the sequence is: {next_value}")
    print("Visual representation of the sequences:")
    for sequence in history:
        print("   " * (len(history) - len(sequence)), "   ".join(map(str, sequence)))

print(f"The sum of all next values is: {total}")