
with open("input1.txt", "r") as open_file:
    lines = open_file.readlines()

total = 0

for line in lines:
    first_digit_string = ""
    second_digit_string = ""

    for chr in line:
        if chr.isdigit():
            first_digit_string = chr
            break

    for chr in reversed(line):
        if chr.isdigit():
            second_digit_string = chr
            break

    line_digit = int(first_digit_string + second_digit_string)
    total += line_digit

print(total)
