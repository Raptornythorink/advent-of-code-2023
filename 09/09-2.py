def find_next_value(history: list[int]) -> int:
    sequences = [history]

    while any(x != 0 for x in sequences[-1]):
        sequences.append(
            [
                sequences[-1][i] - sequences[-1][i - 1]
                for i in range(1, len(sequences[-1]))
            ]
        )

    sequences[-1][-1] = 0
    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][0] - sequences[i + 1][-1])

    return sequences[0][-1]


def main():
    histories: list[list[int]] = []
    next_values = []

    with open("./input", "r") as file:
        for line in file:
            histories.append([int(x) for x in line.strip().split()])

    for history in histories:
        next_values.append(find_next_value(history))

    print(next_values)
    print(sum(next_values))


if __name__ == "__main__":
    main()
