def get_hash(string: str) -> int:
    value = 0
    for char in string:
        value = (value + ord(char)) * 17 % 256
    return value


def remove_lens(lst: list[tuple[str, int]], label: str):
    for i in range(len(lst)):
        if lst[i][0] == label:
            lst.pop(i)
            return


def insert_lens(lst: list[tuple[str, int]], label: str, focal_length: int):
    for i in range(len(lst)):
        if lst[i][0] == label:
            lst[i] = (label, focal_length)
            return
    lst.append((label, focal_length))


def main():
    with open("./input", "r") as file:
        steps = file.read().strip().split(",")

    hashmap = {i: [] for i in range(256)}

    for step in steps:
        if "-" in step:
            label = step.split("-")[0]
            hash = get_hash(label)
            remove_lens(hashmap[hash], label)
        else:
            label, focal_length = step.split("=")
            hash = get_hash(label)
            insert_lens(hashmap[hash], label, int(focal_length))

    focusing_power = sum(
        (box_number + 1) * (slot_number + 1) * focal_length
        for box_number in range(255)
        for slot_number, (_, focal_length) in enumerate(hashmap[box_number])
    )

    print(focusing_power)


if __name__ == "__main__":
    main()
