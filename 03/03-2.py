from typing import List, Tuple

def main():
    numbers: List[int] = []
    numbers_pos: List[List[Tuple[int, int]]] = []
    gear_symbols_pos: List[Tuple[int, int]] = []
    gear_ratio = 0

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
                    if char == "*":
                        gear_symbols_pos.append((i, j))
            if current_number:
                numbers.append(int(current_number))
                numbers_pos.append(current_number_pos)

    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
             (1, -1), (1, 0), (1, 1)]

    for gear_symbol_pos in gear_symbols_pos:
        adjacent_part_numbers = []
        for number, number_pos in zip(numbers, numbers_pos):
            over = False
            for i, j in number_pos:
                for di, dj in moves:
                    if (i + di, j + dj) == gear_symbol_pos:
                        adjacent_part_numbers.append(number)
                        over = True
                        break
                if over:
                    break
        if len(adjacent_part_numbers) == 2:
            gear_ratio += adjacent_part_numbers[0] * adjacent_part_numbers[1]
    
    print(gear_ratio)

if __name__ == "__main__":
    main()
