def get_hand_value(card_values: dict[str, int], hand: str) -> int:
    return sum([(13 ** (4 - i)) * card_values[card] for i, card in enumerate(hand)])


def get_hand_strength(hand: str) -> int:
    cards: dict[str, int] = {}
    joker_number = 0
    for card in hand:
        if card == "J":
            joker_number += 1
        elif card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    cards_numbers = sorted(cards.values(), reverse=True)

    if joker_number == 5 or cards_numbers[0] + joker_number == 5:
        return 6
    elif cards_numbers[0] + joker_number == 4:
        return 5
    elif cards_numbers[0] + joker_number == 3 and cards_numbers[1] == 2:
        return 4
    elif cards_numbers[0] + joker_number == 3:
        return 3
    elif cards_numbers[0] == 2 and cards_numbers[1] + joker_number == 2:
        return 2
    elif cards_numbers[0] + joker_number == 2:
        return 1
    else:
        return 0


def main():
    hands_and_bids: tuple[str, int] = []
    card_values = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "J": 0,
    }
    with open("./input", "r") as file:
        for line in file:
            hand_and_bid = line.strip().split()
            hands_and_bids.append((hand_and_bid[0], int(hand_and_bid[1])))
    hands_and_bids.sort(
        key=lambda hand_and_bid: (13 ** 5) * get_hand_strength(hand_and_bid[0])
        + get_hand_value(card_values, hand_and_bid[0]),
    )
    winnin_gains = sum(
        [hand_and_bid[1] * (i + 1) for i, hand_and_bid in enumerate(hands_and_bids)]
    )

    print(winnin_gains)


if __name__ == "__main__":
    main()
