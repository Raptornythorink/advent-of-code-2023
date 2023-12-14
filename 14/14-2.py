def get_north_tilted_grid(grid: list[list[str]]) -> list[list[str]]:
    n, m = len(grid), len(grid[0])
    tilted_grid: list[list[str]] = [[x for x in row] for row in grid]
    for i in range(1, n):
        for j in range(m):
            if grid[i][j] == "O":
                row, col = i, j
                while row > 0 and tilted_grid[row - 1][col] == ".":
                    row -= 1
                tilted_grid[i][j] = "."
                tilted_grid[row][col] = "O"
    return tilted_grid


def get_south_tilted_grid(grid: list[list[str]]) -> list[list[str]]:
    n, m = len(grid), len(grid[0])
    tilted_grid: list[list[str]] = [[x for x in row] for row in grid]
    for i in range(n - 2, -1, -1):
        for j in range(m):
            if grid[i][j] == "O":
                row, col = i, j
                while row < n - 1 and tilted_grid[row + 1][col] == ".":
                    row += 1
                tilted_grid[i][j] = "."
                tilted_grid[row][col] = "O"
    return tilted_grid


def get_west_tilted_grid(grid: list[list[str]]) -> list[list[str]]:
    n, m = len(grid), len(grid[0])
    tilted_grid: list[list[str]] = [[x for x in row] for row in grid]
    for i in range(n):
        for j in range(1, m):
            if grid[i][j] == "O":
                row, col = i, j
                while col > 0 and tilted_grid[row][col - 1] == ".":
                    col -= 1
                tilted_grid[i][j] = "."
                tilted_grid[row][col] = "O"
    return tilted_grid


def get_east_tilted_grid(grid: list[list[str]]) -> list[list[str]]:
    n, m = len(grid), len(grid[0])
    tilted_grid: list[list[str]] = [[x for x in row] for row in grid]
    for i in range(n):
        for j in range(m - 2, -1, -1):
            if grid[i][j] == "O":
                row, col = i, j
                while col < m - 1 and tilted_grid[row][col + 1] == ".":
                    col += 1
                tilted_grid[i][j] = "."
                tilted_grid[row][col] = "O"
    return tilted_grid


def get_cycle_tilted_grid(grid: list[list[str]]) -> list[list[str]]:
    return get_east_tilted_grid(
        get_south_tilted_grid(get_west_tilted_grid(get_north_tilted_grid(grid)))
    )


def calc_load(grid: list[list[str]]) -> int:
    n, m = len(grid), len(grid[0])
    return sum(n - i for i in range(n) for j in range(m) if grid[i][j] == "O")


def find_period(lst: list) -> int:
    n = len(lst)
    for period in range(1, n // 2 + 1):
        if all(lst[i] == lst[i - period] for i in range(period, n)):
            return period
    return n


def main():
    grid: list[list[str]] = []
    with open("./input", "r") as file:
        for line in file:
            grid.append(list(line.strip()))

    sample_length = len(grid) + len(grid[0])
    total_cycles = 1000000000

    for _ in range(sample_length):
        grid = get_cycle_tilted_grid(grid)

    loads = []
    for _ in range(sample_length):
        grid = get_cycle_tilted_grid(grid)
        loads.append(calc_load(grid))

    period = find_period(loads)
    final_load = loads[(total_cycles - sample_length) % period - 1]

    print(final_load)


if __name__ == "__main__":
    main()
