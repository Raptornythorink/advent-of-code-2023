def row_symetry(pattern: list[str]) -> int:
    n = len(pattern)
    for i in range(1, n):
        mirror_length = min(i, n - i)
        if pattern[i - mirror_length : i] == list(
            reversed(pattern[i : i + mirror_length])
        ):
            return i
    return 0


def main():
    patterns: list[list[str]] = []
    current_pattern: list[str] = []
    with open("./input", "r") as file:
        for line in file:
            if line == "\n":
                patterns.append(current_pattern)
                current_pattern = []
            else:
                current_pattern.append(line.strip())
        patterns.append(current_pattern)

    result = sum(
        100 * row_symetry(pattern) + row_symetry(list(zip(*pattern)))
        for pattern in patterns
    )

    print(result)


if __name__ == "__main__":
    main()
