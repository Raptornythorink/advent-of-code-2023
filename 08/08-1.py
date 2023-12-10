def main():
    next_nodes: dict[str, tuple[str, str]] = {}
    with open("./input", "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                instructions = line.strip()
                n_instructions = len(instructions)
            if i > 1:
                next_nodes[line[0:3]] = (line[7:10], line[12:15])

    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        if instructions[steps % n_instructions] == "L":
            current_node = next_nodes[current_node][0]
        else:
            current_node = next_nodes[current_node][1]
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
