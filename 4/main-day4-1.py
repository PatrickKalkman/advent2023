
def read_input_file():
    with open("input1.txt", "r") as open_file:
        lines = open_file.readlines()

    return lines


# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

def parse_lines(lines):
    total = 0
    for line in lines:
        card_numbers = line.strip().split(':')
        numbers = card_numbers[1].split('|')
        winning_numbers = numbers[0].split()
        my_numbers = numbers[1].split()
        result = 0
        for number in my_numbers:
            if number in winning_numbers:
                if result == 0:
                    result = 1
                else:
                    result *= 2
                print(f'Found {number} in {winning_numbers}')
        total += result
    return total


lines = read_input_file()
total = parse_lines(lines)
print(total)
