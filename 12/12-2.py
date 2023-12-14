from functools import cache


@cache
def get_valid_arrangements_number(springs: str, groups: tuple[int]) -> int:
    if not springs:
        return 1 * (not groups)
    if not groups:
        return 1 * (not any(spring == "#" for spring in springs))
    if len(springs) < groups[0]:
        return 0

    if springs[0] == ".":
        return get_valid_arrangements_number(springs[1:], groups)
    elif springs[0] == "#":
        if any(spring == "." for spring in springs[: groups[0]]):
            return 0
        if len(springs) == groups[0]:
            return 1 * (len(groups) == 1)
        if springs[groups[0]] == "#":
            return 0
        return get_valid_arrangements_number(springs[groups[0] + 1 :], groups[1:])
    return get_valid_arrangements_number(
        springs[1:], groups
    ) + get_valid_arrangements_number("#" + springs[1:], groups)


def main():
    all_springs: list[str] = []
    all_groups: list[tuple[int]] = []

    with open("./input", "r") as file:
        for line in file:
            springs, groups = "", []
            for _ in range(4):
                springs += line.strip().split()[0] + "?"
                groups += list(map(int, line.strip().split()[1].split(",")))
            springs += line.strip().split()[0]
            groups += list(map(int, line.strip().split()[1].split(",")))
            all_springs.append(springs)
            all_groups.append(tuple(groups))

    total_arrangements = sum(
        get_valid_arrangements_number(springs, groups)
        for springs, groups in zip(all_springs, all_groups)
    )

    print(total_arrangements)


if __name__ == "__main__":
    main()
