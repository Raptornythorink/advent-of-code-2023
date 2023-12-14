def get_tilted_grid(grid: list[list[str]]) -> list[list[str]]:
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


def calc_load(grid: list[list[str]]) -> int:
    n, m = len(grid), len(grid[0])
    return sum(n - i for i in range(n) for j in range(m) if grid[i][j] == "O")


def main():
    grid: list[list[str]] = []
    with open("./input", "r") as file:
        for line in file:
            grid.append(list(line.strip()))

    titled_grid = get_tilted_grid(grid)
    load = calc_load(titled_grid)
    print(load)

    for row in titled_grid:
        print("".join(row))


if __name__ == "__main__":
    main()
