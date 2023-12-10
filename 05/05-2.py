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
                source_range_start + range_length,
                destination_range_start,
            )
        )
        i += 1
    mapping.sort()
    i += 2
    return mapping, i


def get_mapping_value(mapping: list[tuple[int, int, int]], value: int) -> int:
    for source_range_start, source_range_end, destination_range_start in mapping:
        if source_range_start <= value < source_range_end:
            return destination_range_start + value - source_range_start
    return value


def get_new_segments(
    mapping: list[tuple[int, int, int]], segments: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    new_segments = []
    i_segment = 0
    i_mapping = 0
    segment_start, segment_end = segments[0]
    mapping_start, mapping_end, _ = mapping[0]

    while i_segment < len(segments) and i_mapping < len(mapping):
        if segment_end <= mapping_start:
            new_segments.append((segment_start, segment_end))
            i_segment += 1
            if i_segment < len(segments):
                segment_start, segment_end = segments[i_segment]
        elif mapping_end <= segment_start:
            i_mapping += 1
            if i_mapping < len(mapping):
                mapping_start, mapping_end, _ = mapping[i_mapping]
        elif segment_start <= mapping_start <= mapping_end <= segment_end:
            new_segments.append((segment_start, mapping_start))
            new_segments.append((mapping_start, mapping_end))
            segment_start = mapping_end
            i_mapping += 1
            if i_mapping < len(mapping):
                mapping_start, mapping_end, _ = mapping[i_mapping]
        elif mapping_start <= segment_start <= segment_end <= mapping_end:
            new_segments.append((segment_start, segment_end))
            i_segment += 1
            if i_segment < len(segments):
                segment_start, segment_end = segments[i_segment]
        elif segment_start <= mapping_start <= segment_end <= mapping_end:
            new_segments.append((segment_start, mapping_start))
            new_segments.append((mapping_start, segment_end))
            mapping_start = segment_end
            i_segment += 1
            if i_segment < len(segments):
                segment_start, segment_end = segments[i_segment]
        elif mapping_start <= segment_start <= mapping_end <= segment_end:
            new_segments.append((segment_start, mapping_end))
            segment_start = mapping_end
            i_mapping += 1
            if i_mapping < len(mapping):
                mapping_start, mapping_end, _ = mapping[i_mapping]

    while i_segment < len(segments):
        new_segments.append((segment_start, segment_end))
        i_segment += 1
        if i_segment < len(segments):
            segment_start, segment_end = segments[i_segment]

    return new_segments


def main():
    with open("./input", "r") as file:
        lines = file.readlines()

    seeds_info = list(map(int, lines[0].strip().split(":")[1].split()))
    segments = sorted(
        [
            (seeds_info[i], seeds_info[i] + seeds_info[i + 1])
            for i in range(0, len(seeds_info), 2)
        ]
    )

    i = 3
    mappings: list[list[tuple[int, int, int]]] = []
    for _ in range(7):
        mapping, i = generate_mapping(lines, i)
        mappings.append(mapping)

    for mapping in mappings:
        segments = sorted(
            [
                (
                    mapped_start_value := get_mapping_value(mapping, segment[0]),
                    segment[1] - segment[0] + mapped_start_value,
                )
                for segment in get_new_segments(mapping, segments)
            ]
        )

    min_location = min(segments, key=lambda segment: segment[0])[0]

    print(min_location)


if __name__ == "__main__":
    main()
