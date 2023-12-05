def main():
    powers = []
    with open("./input", "r") as file:
        for line in file:
            game_inputs = line.strip().split(": ")[1].split("; ")
            min_red = 0
            min_green = 0
            min_blue = 0
            for game_input in game_inputs:
                round_inputs = game_input.split(", ")
                for round_input in round_inputs:
                    number, color = round_input.split(" ")
                    if color == "red":
                        min_red = max(min_red, int(number))
                    elif color == "green":
                        min_green = max(min_green, int(number))
                    elif color == "blue":
                        min_blue = max(min_blue, int(number))
            powers.append(min_red * min_green * min_blue)
    print(sum(powers))


if __name__ == "__main__":
    main()
