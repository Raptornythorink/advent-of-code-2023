def main():
    won_cards = {}

    with open("./input", "r") as file:
        for i, line in enumerate(file):
            matches = 0
            winning_numbers, numbers = map(
                lambda x: x.split(), line.strip().split(": ")[1].split("|")
            )
            winning_numbers = set(winning_numbers)
            for number in numbers:
                if number in winning_numbers:
                    matches += 1
            won_cards[i] = range(i + 1, i + 1 + matches)
    card_number = i

    points = {i: 1 for i in range(card_number + 1)}

    for i in range(card_number, -1, -1):
        if i in won_cards:
            for j in won_cards[i]:
                if j in points:
                    points[i] += points[j]

    print(sum(points.values()))


if __name__ == "__main__":
    main()
