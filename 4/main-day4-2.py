from collections import deque


def read_input_file():
    with open("input2.txt", "r") as open_file:
        lines = open_file.readlines()

    return lines


# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

def parse_lines(lines):
    cards = {}
    for line in lines:
        card_numbers = line.strip().split(':')
        numbers = card_numbers[1].split('|')
        winning_numbers = numbers[0].split()
        my_numbers = numbers[1].split()
        cards[int(card_numbers[0].replace('Card', ' ').strip())] = (1, winning_numbers, my_numbers)

    return cards


def process_cards(cards):
    # Initialize the queue with the original card structures
    queue = deque([card_id for card_id in cards])

    # Dictionary to keep track of the total number of each card
    total_cards = {card_id: 0 for card_id in cards}

    while queue:
        card_id = queue.popleft()
        total_cards[card_id] += 1

        winning_numbers_list, my_numbers = cards[card_id][1], cards[card_id][2]
        winning_count = sum(1 for number in my_numbers if number in winning_numbers_list)

        # Add copies of subsequent cards to the queue
        for adder in range(card_id + 1, card_id + 1 + winning_count):
            if adder in cards:
                queue.append(adder)

    return total_cards



lines = read_input_file()
cards = parse_lines(lines)
cards = process_cards(cards)
print(cards)
print(sum(cards.values()))
