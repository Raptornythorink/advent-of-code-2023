def roots(a: int, b: int, c: int) -> tuple[float, float]:
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (
        -b - (b ** 2 - 4 * a * c) ** 0.5
    ) / (2 * a)


def main():
    with open("./input", "r") as file:
        lines = file.readlines()
        times = map(int, lines[0].strip().split(":")[1].split())
        distances = map(int, lines[1].strip().split(":")[1].split())

    score = 1

    for time, distance in zip(times, distances):
        x1, x2 = roots(-1, time, -distance)
        winning_attempts = int(x2) - int(x1)
        score *= winning_attempts

    print(score)


if __name__ == "__main__":
    main()
