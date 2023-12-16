def read_input_file():
    with open("./input1.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_items(lines):
    items = []
    for line in lines:
        # Split line into items based on commas
        line_items = line.strip().split(",")
        # Further split each item into its characters and append to items
        for item in line_items:
            items.append([char for char in item])
    return items


def calculate_hash(item):
    item_value = 0
    for char in item:
        # Convert char to ASCII code
        item_value += ord(char)
        item_value *= 17

    remainder = item_value % 256
    return remainder


def calculate_hash_total(items):
    total = 0
    for item in items:
        remainder = calculate_hash(item)
        # print("Item:", item, "Remainder:", remainder)
        total += remainder
    return total


lines = read_input_file()
items = parse_items(lines)
total = calculate_hash_total(items)
print(total)
