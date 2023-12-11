def main():
    with open("./input", "r") as file:
        grid = [list(line.strip()) for line in file]

    expansion_factor = 2

    row_distances = {
        i: expansion_factor if all(cell == "." for cell in grid[i]) else 1
        for i in range(len(grid))
    }
    col_distances = {
        j: expansion_factor if all(row[j] == "." for row in grid) else 1
        for j in range(len(grid[0]))
    }

    galaxies = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if grid[i][j] != "."
    ]

    total_length = sum(
        sum(
            row_distances[row]
            for row in range(
                *sorted([galaxies[i][0], galaxies[j][0]]),
            )
        )
        + sum(
            col_distances[col]
            for col in range(
                *sorted([galaxies[i][1], galaxies[j][1]]),
            )
        )
        for i in range(len(galaxies))
        for j in range(i)
    )

    print(total_length)


if __name__ == "__main__":
    main()
