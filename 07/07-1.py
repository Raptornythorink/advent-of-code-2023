def get_hand_value(card_values: dict[str, int], hand: str) -> int:
    return sum([(13 ** (4 - i)) * card_values[card] for i, card in enumerate(hand)])


def get_hand_strength(hand: str) -> int:
    cards: dict[str, int] = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    cards_numbers = sorted(cards.values(), reverse=True)

    if cards_numbers[0] == 5:
        return 6
    elif cards_numbers[0] == 4:
        return 5
    elif cards_numbers[0] == 3 and cards_numbers[1] == 2:
        return 4
    elif cards_numbers[0] == 3:
        return 3
    elif cards_numbers[0] == 2 and cards_numbers[1] == 2:
        return 2
    elif cards_numbers[0] == 2:
        return 1
    else:
        return 0


def main():
    hands_and_bids: tuple[str, int] = []
    card_values = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "J": 9,
        "T": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
        "2": 0,
    }
    with open("./input", "r") as file:
        for line in file:
            hand_and_bid = line.strip().split()
            hands_and_bids.append((hand_and_bid[0], int(hand_and_bid[1])))
    hands_and_bids.sort(
        key=lambda hand_and_bid: (13 ** 5) * get_hand_strength(hand_and_bid[0])
        + get_hand_value(card_values, hand_and_bid[0]),
    )
    winning_gains = sum(
        [hand_and_bid[1] * (i + 1) for i, hand_and_bid in enumerate(hands_and_bids)]
    )

    print(winning_gains)


if __name__ == "__main__":
    main()
