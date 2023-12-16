def beam_path(
    grid: list[str],
    energized: dict[tuple[int, int], set[str]],
    x: int,
    y: int,
    direction: str,
    direction_map: dict[tuple[str, str], tuple[str]],
    n: int,
    m: int,
):
    if (x, y) in energized:
        if direction in energized[(x, y)]:
            return
        energized[(x, y)].append(direction)

    if direction == "right":
        x += 1
        while x < m and grid[y][x] == ".":
            energized[(x, y)].append(direction)
            x += 1
        if x < m:
            for next_direction in direction_map[(direction, grid[y][x])]:
                beam_path(grid, energized, x, y, next_direction, direction_map, n, m)

    elif direction == "left":
        x -= 1
        while x >= 0 and grid[y][x] == ".":
            energized[(x, y)].append(direction)
            x -= 1
        if x >= 0:
            for next_direction in direction_map[(direction, grid[y][x])]:
                beam_path(grid, energized, x, y, next_direction, direction_map, n, m)

    elif direction == "down":
        y += 1
        while y < n and grid[y][x] == ".":
            energized[(x, y)].append(direction)
            y += 1
        if y < n:
            for next_direction in direction_map[(direction, grid[y][x])]:
                beam_path(grid, energized, x, y, next_direction, direction_map, n, m)

    elif direction == "up":
        y -= 1
        while y >= 0 and grid[y][x] == ".":
            energized[(x, y)].append(direction)
            y -= 1
        if y >= 0:
            for next_direction in direction_map[(direction, grid[y][x])]:
                beam_path(grid, energized, x, y, next_direction, direction_map, n, m)


def get_initial_energized(n: int, m: int) -> dict[tuple[int, int], list[str]]:
    return {(x, y): [] for y in range(n) for x in range(m)}


def get_energized_tiles(energized: dict[tuple[int, int], list[str]]) -> int:
    return len([True for x, y in energized if len(energized[(x, y)])])


def main():
    grid: list[list[str]] = []
    with open("./input", "r") as file:
        for line in file:
            grid.append(line.strip())

    most_energized = 0
    n, m = len(grid), len(grid[0])
    direction_map = {
        ("right", "-"): ("right",),
        ("right", "/"): ("up",),
        ("right", "\\"): ("down",),
        ("right", "|"): ("up", "down"),
        ("left", "-"): ("left",),
        ("left", "/"): ("down",),
        ("left", "\\"): ("up",),
        ("left", "|"): ("up", "down"),
        ("down", "|"): ("down",),
        ("down", "/"): ("left",),
        ("down", "\\"): ("right",),
        ("down", "-"): ("right", "left"),
        ("up", "|"): ("up",),
        ("up", "/"): ("right",),
        ("up", "\\"): ("left",),
        ("up", "-"): ("right", "left"),
    }

    for y in range(n):
        energized = get_initial_energized(n, m)
        beam_path(grid, energized, -1, y, "right", direction_map, n, m)
        most_energized = max(most_energized, get_energized_tiles(energized))

        energized = get_initial_energized(n, m)
        beam_path(grid, energized, m, y, "left", direction_map, n, m)
        most_energized = max(most_energized, get_energized_tiles(energized))

    for x in range(m):
        energized = get_initial_energized(n, m)
        beam_path(grid, energized, x, -1, "down", direction_map, n, m)
        most_energized = max(most_energized, get_energized_tiles(energized))

        energized = get_initial_energized(n, m)
        beam_path(grid, energized, x, n, "up", direction_map, n, m)
        most_energized = max(most_energized, get_energized_tiles(energized))

    print(most_energized)


if __name__ == "__main__":
    main()
