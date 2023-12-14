from itertools import product


def is_valid(springs: str, groups: list[int]) -> bool:
    return list(map(len, [group for group in springs.split(".") if group])) == groups


def get_valid_arrangements_number(springs: str, groups: list[int]) -> int:
    n_unkown = springs.count("?")
    arrangements = product([".", "#"], repeat=n_unkown)
    valid_arrangements = 0
    for arrangement in arrangements:
        replaced_springs = springs
        for char in arrangement:
            replaced_springs = replaced_springs.replace("?", char, 1)
        if is_valid(replaced_springs, groups):
            valid_arrangements += 1
    return valid_arrangements


def main():
    all_springs: list[str] = []
    all_groups: list[list[int]] = []

    with open("./input", "r") as file:
        for line in file:
            all_springs.append(line.strip().split()[0])
            all_groups.append(list(map(int, line.strip().split()[1].split(","))))

    total_arrangements = 0
    for springs, groups in zip(all_springs, all_groups):
        total_arrangements += get_valid_arrangements_number(springs, groups)
    print()
    print(total_arrangements)


from time import time

if __name__ == "__main__":
    start = time()
    main()
    print("Time:", time() - start)
