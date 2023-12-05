def get_digit(line: str, i: int, n: int) -> int or None:
    if i < n:
        if line[i].isdigit():
            return int(line[i])
        if i + 3 <= n:
            if line[i : i + 3] == "one":
                return 1
            if line[i : i + 3] == "two":
                return 2
            if line[i : i + 3] == "six":
                return 6
            if i + 4 <= n:
                if line[i : i + 4] == "four":
                    return 4
                if line[i : i + 4] == "five":
                    return 5
                if line[i : i + 4] == "nine":
                    return 9
                if i + 5 <= n:
                    if line[i : i + 5] == "zero":
                        return 0
                    if line[i : i + 5] == "eight":
                        return 8
                    if line[i : i + 5] == "three":
                        return 3
                    if line[i : i + 5] == "seven":
                        return 7


def main():
    with open("./input", "r") as file:
        total = 0
        for line in file:
            n = len(line)
            digits = list(
                filter(
                    lambda x: x is not None, [get_digit(line, i, n) for i in range(n)]
                )
            )
            if digits:
                total += 10 * digits[0] + digits[-1]
    print(total)


if __name__ == "__main__":
    main()
