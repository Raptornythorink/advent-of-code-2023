def roots(a: int, b: int, c: int) -> tuple[float, float]:
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (
        -b - (b ** 2 - 4 * a * c) ** 0.5
    ) / (2 * a)


def main():
    with open("./input", "r") as file:
        lines = file.readlines()
        time_string = ""
        for char in lines[0].strip():
            if char.isdigit():
                time_string += char
        time = int(time_string)
        distance_string = ""
        for char in lines[1].strip():
            if char.isdigit():
                distance_string += char
        distance = int(distance_string)

    x1, x2 = roots(-1, time, -distance)
    winning_attempts = int(x2) - int(x1)

    print(winning_attempts)


if __name__ == "__main__":
    main()
