from typing import List, Set, Tuple

def main():
    numbers: List[int] = []
    numbers_pos: List[List[Tuple[int, int]]] = []
    symbols_pos: Set[Tuple[int, int]] = set()
    part_numbers: List[int] = []

    with open("./input", "r") as file:
        for i, line in enumerate(file):
            current_number = ""
            current_number_pos = []
            for j, char in enumerate(line.strip()):
                if char.isdigit():
                    current_number += char
                    current_number_pos.append((i, j))
                else:
                    if current_number:
                        numbers.append(int(current_number))
                        numbers_pos.append(current_number_pos)
                        current_number = ""
                        current_number_pos = []
                    if char != ".":
                        symbols_pos.add((i, j))
            if current_number:
                numbers.append(int(current_number))
                numbers_pos.append(current_number_pos)

    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]

    for number, number_pos in zip(numbers, numbers_pos):
        over = False
        for i, j in number_pos:
            for di, dj in moves:
                if (i + di, j + dj) in symbols_pos:
                    part_numbers.append(number)
                    over = True
                    break
            if over:
                break
    
    print(sum(part_numbers))

if __name__ == "__main__":
    main()
