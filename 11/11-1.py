def main():
    with open("./input", "r") as file:
        grid = [list(line.strip()) for line in file]

    i = 0
    while i < len(grid):
        if all(cell == "." for cell in grid[i]):
            grid.insert(i, grid[i])
            i += 2
        else:
            i += 1

    j = 0
    while j < len(grid[0]):
        if all(row[j] == "." for row in grid):
            for row in grid:
                row.insert(j, row[j])
            j += 2
        else:
            j += 1

    galaxies = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if grid[i][j] != "."
    ]

    total_length = sum(
        abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        for i in range(len(galaxies))
        for j in range(i)
    )

    print(total_length)


if __name__ == "__main__":
    main()
