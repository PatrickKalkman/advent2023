def read_input_file():
    with open("./input1.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_blocks(lines):
    blocks = []
    current_block = []

    for line in lines:
        if line.strip():
            current_block.append(list(line.strip()))
        else:
            if current_block:
                blocks.append(current_block)
                current_block = []

    if current_block:
        blocks.append(current_block)

    return blocks


def find_horizontal_reflection(block):
    rows = len(block)

    def is_mirror_pair(row1, row2):
        return row1 == row2

    for i in range(rows - 1):
        # print("comparing")
        # print("".join(block[i]) + " " + str(i))
        # print("".join(block[i + 1]) + " " + str(i + 1))
        if is_mirror_pair(block[i], block[i + 1]):
            #print("Found a mirror pair! at row", i, "and", i + 1)
            top = i - 1
            bottom = i + 2

            # Expand the search outward
            while top >= 0 and bottom < rows and is_mirror_pair(block[top], block[bottom]):
                top -= 1
                bottom += 1

            #print("top", top, "bottom", bottom)
            #print(rows)

            # Check if the reflection is valid
            if top == 0 and bottom == rows:
                return i, i + 1
            elif top == -1:
                return i, i + 1
            elif bottom == rows and top > 0:
                return i, i + 1

    return None, None


def find_vertical_reflection(block):
    cols = len(block[0])

    def is_mirror_pair(col1, col2):
        return col1 == col2

    # Extract columns from block
    def get_column(block, col_idx):
        return [row[col_idx] for row in block]

    for i in range(cols - 1):
        col1 = get_column(block, i)
        col2 = get_column(block, i + 1)
        # print("".join(col1) + " " + str(i))
        # print("".join(col2) + " " + str(i + 1))
        if is_mirror_pair(col1, col2):
            #print("Found a mirror pair! at column", i, "and", i + 1)
            left = i - 1
            right = i + 2

            # Expand the search outward
            while left >= 0 and right < cols and is_mirror_pair(get_column(block, left), get_column(block, right)):
                left -= 1
                right += 1

            #print("left", left, "right", right)
            #print(cols)

            # Check if the reflection is valid
            if left == 0 and right == cols:
                return i, i + 1
            if left == -1:
                return i, i + 1
            elif right == cols and left > 0:
                return i, i + 1

    return None, None


def calculate_pattern_score(block):
    horizontal_reflection = find_horizontal_reflection(block)
    vertical_reflection = find_vertical_reflection(block)

    score = 0
    if horizontal_reflection != (None, None):
        score += 100 * (horizontal_reflection[0] + 1)
    elif vertical_reflection != (None, None):
        score += vertical_reflection[0] + 1

    return score


lines = read_input_file()
blocks = parse_blocks(lines)
sum = 0
for block in blocks:
    row1, row2 = find_horizontal_reflection(block)
    score = calculate_pattern_score(block)
    sum += score
    if (row1 is None) or (row2 is None):
        col1, col2 = find_vertical_reflection(block)
        if (col1 is None) or (col2 is None):
            print("no reflection found")
        else:
            print("found vertical reflection at", col1, col2)
    else:
        print("found horizontal reflection at", row1, row2)

print(sum)
