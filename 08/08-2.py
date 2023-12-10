from math import lcm


def main():
    next_nodes: dict[str, tuple[str, str]] = {}
    with open("./input", "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                instructions = line.strip()
                n_instructions = len(instructions)
            if i > 1:
                next_nodes[line[0:3]] = (line[7:10], line[12:15])

    current_nodes = [node for node in next_nodes if node[2] == "A"]
    ending_nodes = set([node for node in next_nodes if node[2] == "Z"])
    path_lengths = [-1 for _ in range(len(current_nodes))]
    steps = 0

    while not all(path_length > 0 for path_length in path_lengths):
        if instructions[steps % n_instructions] == "L":
            current_nodes = list(map(lambda node: next_nodes[node][0], current_nodes))
        else:
            current_nodes = list(map(lambda node: next_nodes[node][1], current_nodes))
        for i, node in enumerate(current_nodes):
            if node in ending_nodes:
                path_lengths[i] = steps + 1
        steps += 1

    print(lcm(*path_lengths))


if __name__ == "__main__":
    main()
