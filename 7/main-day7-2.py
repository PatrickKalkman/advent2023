from collections import Counter
from functools import cmp_to_key


def read_input_file():
    with open("input2.txt", "r") as open_file:
        lines = open_file.readlines()
    return lines


def parse_hands(lines):
    hands = []
    for line in lines:
        parts = line.split()
        hands.append((parts[0], int(parts[1])))
    return hands


def determine_hand_type_and_order(hand):
    def hand_order(frequencies):
        if 5 in frequencies:
            return 7  # Five of a kind
        elif 4 in frequencies:
            return 6  # Four of a kind
        elif 3 in frequencies and 2 in frequencies:
            return 5  # Full house
        elif 3 in frequencies:
            return 4  # Three of a kind
        elif sorted(frequencies) == [1, 2, 2]:
            return 3  # Two pair
        elif list(frequencies).count(2) == 1:
            return 2  # One pair
        else:
            return 1  # High card

    # If there are no jokers in the hand, return the regular hand order
    if 'J' not in hand:
        return hand_order(Counter(hand).values())

    # All possible cards the joker could represent, excluding cards already in hand
    possible_replacements = [card for card in "AKQJT98765432"]

    # Evaluate the hand for each possible replacement of the joker
    best_order = 0
    for replacement in possible_replacements:
        new_hand = hand.replace('J', replacement)
        best_order = max(best_order, hand_order(Counter(new_hand).values()))

    return best_order


def card_strength(card):
    rank_order = "AKQT98765432J"
    return rank_order.index(card)


def compare_items(hand_a, hand_b):
    # Implement your comparison logic here
    # Return negative if a < b, zero if a == b, positive if a > b
    result_a = determine_hand_type_and_order(hand_a[0])
    result_b = determine_hand_type_and_order(hand_b[0])

    if result_a > result_b:
        return 1
    elif result_a < result_b:
        return -1

    if result_a == result_b:
        for card_a_1, card_b_1 in zip(hand_a[0], hand_b[0]):
            strength_a = card_strength(card_a_1)
            strength_b = card_strength(card_b_1)
            if strength_a > strength_b:
                return -1
            elif strength_b > strength_a:
                return 1

    return 0  # Hands are identical in strength


def sort_hands(hands):
    sorted_hands = sorted(hands, key=cmp_to_key(compare_items))
    return sorted_hands


def add_rank(hands):
    ranked_hands = [(hand[0], hand[1], rank + 1) for rank, hand in enumerate(hands)]
    return ranked_hands


def calculate_total(ranked_hands):
    return sum(hand[1] * hand[2] for hand in ranked_hands)


lines = read_input_file()
hands = parse_hands(lines)
sorted_hands = sort_hands(hands)
hands_ranked = add_rank(sorted_hands)
total = calculate_total(hands_ranked)

print(total)

