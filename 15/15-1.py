def get_hash(string: str) -> int:
    value = 0
    for char in string:
        value = (value + ord(char)) * 17 % 256
    return value


def main():
    with open("./input", "r") as file:
        steps = file.read().strip().split(",")

    result = sum(get_hash(step) for step in steps)

    print(result)


if __name__ == "__main__":
    main()
