from typing import List, Optional

def solve_part_1():
    file_name:str = "inputs/2.txt"
    with  open(file_name, 'r') as f:
        safe: int = 0
        for line in f.readlines():
            numbers: List[int] = [int(x) for x in line.strip().split(' ')]
            is_ascending: bool = numbers[0] < numbers[1]
            previous: int = 0
            for index in range(1, len(numbers)):
                difference: int = abs(numbers[index] - numbers[index - 1])
                if (difference >= 1 and difference <= 3 and (numbers[index - 1] < numbers[index]) == is_ascending) == False:
                    break
            else:
                safe += 1
   
    print(safe)

def is_safe(numbers: List[int]) -> bool:
    is_ascending: bool = numbers[0] < numbers[1]
    previous: int = 0
    for index in range(1, len(numbers)):
        difference: int = abs(numbers[index] - numbers[index - 1])
        if (difference >= 1 and difference <= 3 and (numbers[index - 1] < numbers[index]) == is_ascending) == False:
            break
    else:
        return True
    return False

def solve_part_2():
    file_name:str = "inputs/2.txt"
    with  open(file_name, 'r') as f:
        safe: int = 0
        for line in f.readlines():
            numbers: List[int] = [int(x) for x in line.strip().split(' ')]
            skipped: int = 0
            previous: int = 0
            for index in range(0, len(numbers) + 1):
                new_numbers = [x for idx, x in enumerate(numbers) if idx != index]
                if is_safe(new_numbers):
                    safe += 1
                    break
    return safe


if __name__ == "__main__":
    #solve_part_1()
    print(solve_part_2())
