def valid_combination(number: int, color: str) -> bool:
    if color == "red" and number > 12:
        return False
    if color == "green" and number > 13:
        return False
    if color == "blue" and number > 14:
        return False
    return True


def main():
    possible_games = []
    with open("./input", "r") as file:
        for i, line in enumerate(file):
            possible = True
            game_inputs = line.strip().split(": ")[1].split("; ")
            for game_input in game_inputs:
                round_inputs = game_input.split(", ")
                for round_input in round_inputs:
                    number, color = round_input.split(" ")
                    if not valid_combination(int(number), color):
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                possible_games.append(i + 1)
    print(sum(possible_games))


if __name__ == "__main__":
    main()
