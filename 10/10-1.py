def get_starting_point(grid: list[str]) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                return i, j
    return -1, -1


def get_next_locations(
    grid: list[str], location: tuple[int, int]
) -> list[tuple[int, int]]:
    if grid[location[0]][location[1]] == "|":
        next_locations = [
            (location[0] - 1, location[1]),
            (location[0] + 1, location[1]),
        ]
    elif grid[location[0]][location[1]] == "-":
        next_locations = [
            (location[0], location[1] - 1),
            (location[0], location[1] + 1),
        ]
    elif grid[location[0]][location[1]] == "L":
        next_locations = [
            (location[0] - 1, location[1]),
            (location[0], location[1] + 1),
        ]
    elif grid[location[0]][location[1]] == "J":
        next_locations = [
            (location[0] - 1, location[1]),
            (location[0], location[1] - 1),
        ]
    elif grid[location[0]][location[1]] == "7":
        next_locations = [
            (location[0] + 1, location[1]),
            (location[0], location[1] - 1),
        ]
    elif grid[location[0]][location[1]] == "F":
        next_locations = [
            (location[0] + 1, location[1]),
            (location[0], location[1] + 1),
        ]
    else:
        next_locations = []
    return [
        next_location
        for next_location in next_locations
        if 0 <= next_location[0] < len(grid)
        and 0 <= next_location[1] < len(grid[0])
        and grid[next_location[0]][next_location[1]] != "."
    ]


def get_starting_point_pipe(grid: list[str], location: tuple[int, int]) -> str:
    north, south, west, east = False, False, False, False
    if location in get_next_locations(grid, (location[0] - 1, location[1])):
        north = True
    if location in get_next_locations(grid, (location[0] + 1, location[1])):
        south = True
    if location in get_next_locations(grid, (location[0], location[1] - 1)):
        west = True
    if location in get_next_locations(grid, (location[0], location[1] + 1)):
        east = True

    pipe_from_directions = {
        (True, True, False, False): "|",
        (False, False, True, True): "-",
        (True, False, False, True): "L",
        (True, False, True, False): "J",
        (False, True, True, False): "7",
        (False, True, False, True): "F",
    }

    return pipe_from_directions[(north, south, west, east)]


def main():
    with open("./input", "r") as file:
        grid = [list(line.strip()) for line in file]

    starting_point = get_starting_point(grid)
    grid[starting_point[0]][starting_point[1]] = get_starting_point_pipe(
        grid, starting_point
    )

    seen = {}
    queue = [(starting_point, -1)]

    while queue:
        location, parent_distance = queue.pop(0)
        if location in seen:
            continue
        seen[location] = parent_distance + 1
        for next_location in get_next_locations(grid, location):
            queue.append((next_location, parent_distance + 1))

    print(max(seen.values()))


if __name__ == "__main__":
    main()
