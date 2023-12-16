def read_input_file():
    with open("./input2.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines

def parse_items(lines):
    items = []
    for line in lines:
        line_items = line.strip().split(",")
        for item in line_items:
            items.append(item)
    return items

def calculate_hash(label):
    item_value = 0
    for char in label:
        item_value += ord(char)
        item_value *= 17
    return item_value % 256

def process_sequence(items):
    boxes = [list() for _ in range(256)]  # Initialize 256 empty boxes
    for item in items:
        if '=' in item:
            label, value = item.split('=')
            box_index = calculate_hash(label)
            lens = (label, int(value))
            # Replace or add lens
            replaced = False
            for i, existing_lens in enumerate(boxes[box_index]):
                if existing_lens[0] == label:
                    boxes[box_index][i] = lens
                    replaced = True
                    break
            if not replaced:
                boxes[box_index].append(lens)
        elif '-' in item:
            label = item[:-1]
            box_index = calculate_hash(label)
            # Remove lens if present
            boxes[box_index] = [l for l in boxes[box_index] if l[0] != label]

    return boxes


def calculate_focusing_power(boxes):
    total_power = 0
    for box_index, box in enumerate(boxes):
        for slot, lens in enumerate(box, start=1):
            lens_power = (1 + box_index) * slot * lens[1]
            total_power += lens_power
    return total_power


lines = read_input_file()
items = parse_items(lines)
boxes = process_sequence(items)
total_focusing_power = calculate_focusing_power(boxes)

print(f"Total Focusing Power: {total_focusing_power}")