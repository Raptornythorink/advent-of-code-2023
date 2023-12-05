def main():
    with open("./input", "r") as file:
        total = 0
        for line in file:
            digits = list(filter(lambda x: x.isdigit(), line))
            if digits:
                total += 10 * int(digits[0]) + int(digits[-1])
    print(total)


if __name__ == "__main__":
    main()
