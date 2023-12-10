def generate_mapping(lines: list[str], i: int) -> list[tuple[int, int, int]]:
    mapping = []
    n = len(lines)
    while i < n and lines[i].strip() != "":
        destination_range_start, source_range_start, range_length = map(
            int, lines[i].strip().split()
        )
        mapping.append(
            (
                source_range_start,
                range_length,
                destination_range_start,
            )
        )
        i += 1
    mapping.sort()
    i += 2
    return mapping, i


def get_mapping_value(mapping: list[tuple[int, int, int]], value: int) -> int:
    for source_range_start, range_length, destination_range_start in mapping:
        if source_range_start <= value < source_range_start + range_length:
            return destination_range_start + value - source_range_start
    return value


def get_location(mappings: list[list[tuple[int, int, int]]], seed: int) -> int:
    res = seed
    for mapping in mappings:
        res = get_mapping_value(mapping, res)
    return res


def main():
    with open("./input", "r") as file:
        lines = file.readlines()

    seeds = map(int, lines[0].strip().split(":")[1].split())

    i = 3
    mappings: list[list[tuple[int, int, int]]] = []
    for _ in range(7):
        mapping, i = generate_mapping(lines, i)
        mappings.append(mapping)

    min_location = min(map(lambda seed: get_location(mappings, seed), seeds))

    print(min_location)


if __name__ == "__main__":
    main()
