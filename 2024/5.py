from typing import List, Dict


def solve_part1():
    with open("inputs/5.txt", "r") as file:
        lines: List[str] = file.readlines()
        count = 0
        line_index: int = 0
        ordering: Dict[int, List[int]] = dict()
        while line_index < len(lines):
            line: str = lines[line_index]
            if '|' not in line:
                break
            words = line.split('|')
            left: int = int(words[0])
            right: int = int(words[1])
            if left not in ordering:
                ordering[left] = []
            ordering[left].append(right)
            line_index += 1
        line_index += 1

        while line_index < len(lines):
            line: str = lines[line_index]
            is_line_valid: bool = True
            numbers = [int(x) for x in line.strip().split(",")]
            for index in range(len(numbers)):
                if not is_line_valid:
                    break
                for j in range(index + 1, len(numbers)):
                    if numbers[j] in ordering and numbers[index] in ordering[numbers[j]]:
                        is_line_valid = False
                        break
            if is_line_valid == True:
                middle = len(numbers) // 2
                count += numbers[middle]
            line_index += 1

    return count

def solve_part2():
    with open("inputs/5.txt") as file:
        ordering: Dict[int, List[int]] = dict()
        count = 0
        line_index: int = 0
        lines: List[str] = file.readlines()
        while line_index < len(lines):
            line: str = lines[line_index]
            if '|' not in line:
                break
            words = line.split('|')
            left: int = int(words[0])
            right: int = int(words[1])
            if left not in ordering:
                ordering[left] = []
            ordering[left].append(right)
            line_index += 1
        line_index += 1

        while line_index < len(lines):
            line: str = lines[line_index]
            is_line_valid: bool = True
            numbers = [int(x) for x in line.strip().split(",")]
            for index in range(len(numbers)):
                if not is_line_valid:
                    break
                for j in range(index + 1, len(numbers)):
                    if numbers[j] in ordering and numbers[index] in ordering[numbers[j]]:
                        is_line_valid = False
                        break

            if is_line_valid == False:
                is_ordered: bool = False
                while is_ordered == False:
                    is_ordered = True
                    for index in range(len(numbers) - 1):
                        if numbers[index + 1] in ordering and numbers[index] in ordering[numbers[index + 1]]:
                            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                            is_ordered = False

                middle = len(numbers) // 2
                count += numbers[middle]
            line_index += 1
    return count

if __name__ == "__main__":
    #print(solve_part1())
    print(solve_part2())