def main():
    total_points = 0

    with open("./input", "r") as file:
        for line in file:
            matches = 0
            winning_numbers, numbers = map(
                lambda x: x.split(), line.strip().split(": ")[1].split("|")
            )
            winning_numbers = set(winning_numbers)
            for number in numbers:
                if number in winning_numbers:
                    matches += 1
            if matches >= 1:
                total_points += 2 ** (matches - 1)

    print(total_points)


if __name__ == "__main__":
    main()
