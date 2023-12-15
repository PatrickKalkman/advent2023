def read_input_file():
    with open("./input2.txt", "r") as open_file:
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
        if is_mirror_pair(block[i], block[i + 1]):
            top = i - 1
            bottom = i + 2

            while top >= 0 and bottom < rows and is_mirror_pair(block[top], block[bottom]):
                top -= 1
                bottom += 1

            if top == 0 and bottom == rows:
                return i, i + 1
            elif top == -1:
                return i, i + 1
            elif bottom == rows and top > 0:
                return i, i + 1

    return None, None


def generate_grids(original_grid):
    rows = len(original_grid)
    cols = len(original_grid[0])
    all_grids = []

    for i in range(rows):
        for j in range(cols):
            # Create a deep copy of the original grid to modify
            new_grid = [row[:] for row in original_grid]

            # Toggle the cell
            new_grid[i][j] = toggle_cell(new_grid[i][j])

            # Add the modified grid to the list
            all_grids.append(new_grid)

    return all_grids


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

        if is_mirror_pair(col1, col2):
            #print("found vertical reflection at", i, i + 1)
            left = i - 1
            right = i + 2

            while left >= 0 and right < cols and is_mirror_pair(get_column(block, left), get_column(block, right)):
                left -= 1
                right += 1

            #print("left", left, "right", right, "cols", cols)

            if left == 0 and right == cols:
                return i, i + 1
            if left == -1:
                return i, i + 1
            if right == cols and left > 0:
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


def toggle_cell(cell):
    return '#' if cell == '.' else '.'


def find_changed_reflection(block):
    original_horizontal_reflection = find_horizontal_reflection(block)
    original_vertical_reflection = find_vertical_reflection(block)
    print("original horizontal reflection", original_horizontal_reflection)
    print("original vertical reflection", original_vertical_reflection)
    rows = len(block)
    cols = len(block[0])

    for i in range(rows):
        for j in range(cols):

            block[i][j] = toggle_cell(block[i][j])

            # Check for new reflection
            new_horizontal_reflection = find_horizontal_reflection(block)
            new_vertical_reflection = find_vertical_reflection(block)

            if new_horizontal_reflection == (None, None) and new_vertical_reflection == (None, None):
                block[i][j] = toggle_cell(block[i][j])
                continue

            if new_horizontal_reflection != original_horizontal_reflection or new_vertical_reflection != original_vertical_reflection:
                print(f"Changing cell ({i+1}, {j+1}) resulted in a different reflection at ({new_horizontal_reflection}, {new_vertical_reflection})")
                return (new_horizontal_reflection, new_vertical_reflection)

            # Toggle the cell back
            block[i][j] = toggle_cell(block[i][j])

    print("No cell change resulted in a different reflection")


lines = read_input_file()
blocks = parse_blocks(lines)

sum = 0
block_nr = 0
for block in blocks:
    block_nr += 1
    print("Block", block_nr)
    row1, row2 = find_horizontal_reflection(block)
    col1, col2 = find_vertical_reflection(block)

    find_changed_reflection(block)
    score = calculate_pattern_score(block)
    sum += score

print(sum)
