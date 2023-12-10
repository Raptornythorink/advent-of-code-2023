from sys import setrecursionlimit


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


def get_expanded_grid(
    grid: list[list[str]], loop: list[tuple[str, str]]
) -> list[list[str]]:
    expanded_grid = [
        ["." for _ in range(len(grid[0]) * 3)] for _ in range(len(grid) * 3)
    ]
    for location in loop:
        if grid[location[0]][location[1]] == "|":
            expanded_grid[location[0] * 3][location[1] * 3] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 2] = "."
        elif grid[location[0]][location[1]] == "-":
            expanded_grid[location[0] * 3][location[1] * 3] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 1] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 2] = "#"
            expanded_grid[location[0] * 3 + 2][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 1] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 2] = "."
        elif grid[location[0]][location[1]] == "L":
            expanded_grid[location[0] * 3][location[1] * 3] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 2] = "#"
            expanded_grid[location[0] * 3 + 2][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 1] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 2] = "."
        elif grid[location[0]][location[1]] == "J":
            expanded_grid[location[0] * 3][location[1] * 3] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 1] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 2] = "."
        elif grid[location[0]][location[1]] == "7":
            expanded_grid[location[0] * 3][location[1] * 3] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 1] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 2] = "."
        elif grid[location[0]][location[1]] == "F":
            expanded_grid[location[0] * 3][location[1] * 3] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 1] = "."
            expanded_grid[location[0] * 3][location[1] * 3 + 2] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 1][location[1] * 3 + 2] = "#"
            expanded_grid[location[0] * 3 + 2][location[1] * 3] = "."
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 1] = "#"
            expanded_grid[location[0] * 3 + 2][location[1] * 3 + 2] = "."
    return expanded_grid


def flood_grid(grid: list[list[str]], location: tuple[int, int]) -> list[list[str]]:
    if grid[location[0]][location[1]] == ".":
        grid[location[0]][location[1]] = "O"
        if (
            0 <= location[0] - 1 < len(grid)
            and grid[location[0] - 1][location[1]] == "."
        ):
            grid = flood_grid(grid, (location[0] - 1, location[1]))
        if (
            0 <= location[0] + 1 < len(grid)
            and grid[location[0] + 1][location[1]] == "."
        ):
            grid = flood_grid(grid, (location[0] + 1, location[1]))
        if (
            0 <= location[1] - 1 < len(grid[0])
            and grid[location[0]][location[1] - 1] == "."
        ):
            grid = flood_grid(grid, (location[0], location[1] - 1))
        if (
            0 <= location[1] + 1 < len(grid[0])
            and grid[location[0]][location[1] + 1] == "."
        ):
            grid = flood_grid(grid, (location[0], location[1] + 1))
    return grid


def main():
    with open("./input", "r") as file:
        grid = [list(line.strip()) for line in file]

    setrecursionlimit(9 * len(grid) * len(grid[0]))

    starting_point = get_starting_point(grid)
    grid[starting_point[0]][starting_point[1]] = get_starting_point_pipe(
        grid, starting_point
    )

    seen = {}
    queue = [(starting_point, None)]

    while queue:
        location, parent = queue.pop(0)
        if location in seen:
            continue
        seen[location] = 0 if parent is None else seen[parent] + 1
        for next_location in get_next_locations(grid, location):
            queue.append((next_location, location))

    expanded_grid = get_expanded_grid(grid, seen.keys())
    for i in range(len(expanded_grid)):
        expanded_grid = flood_grid(expanded_grid, (i, 0))
        expanded_grid = flood_grid(expanded_grid, (i, len(expanded_grid[0]) - 1))
    for j in range(len(expanded_grid[0])):
        expanded_grid = flood_grid(expanded_grid, (0, j))
        expanded_grid = flood_grid(expanded_grid, (len(expanded_grid) - 1, j))

    enclosed_tiles = len(
        [
            True
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if expanded_grid[3 * i + 1][3 * j + 1] == "."
        ]
    )

    print(enclosed_tiles)


if __name__ == "__main__":
    main()
