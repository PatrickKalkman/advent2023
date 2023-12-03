number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def read_input_file():
    with open("input2.txt", "r") as open_file:
        lines = open_file.readlines()

    return lines


def detect_digit(line, insert_front):
    first_digit_string = ""
    first_word_digit = ""

    if insert_front:
        line = reversed(line)

    for chr in line:
        if chr.isdigit():
            first_digit_string = chr
            break
        else:
            if insert_front:
                first_word_digit = chr + first_word_digit
            else:
                first_word_digit += chr

            found = False
            for word in number_words:
                if word in first_word_digit:
                    first_digit_string = str(number_words.index(word) + 1)
                    found = True
                    break

            if found:
                break

    return first_digit_string


def process_lines(lines):

    total = 0
    for line in lines:
        first_digit_string = detect_digit(line, False)
        second_digit_string = detect_digit(line, True)
        line_digit = int(first_digit_string + second_digit_string)
        total += line_digit
    return total


input_lines = read_input_file()
total = process_lines(input_lines)
print(total)
