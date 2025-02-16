import math
from functools import lru_cache
from typing import List, Deque, Tuple
from collections import deque


def part1():
    file_path: str = "./inputs/11.txt"
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
        numbers: Deque[int] = deque()
        numbers.extend([int(number) for number in lines[0].strip().split(" ")])

        steps: int = 75
        while steps > 0:
            print(steps)
            length: int = len(numbers)
            while length > 0:
                front: int = numbers.popleft()
                if front == 0:
                    numbers.append(1)
                elif len(str(front)) % 2 == 0:
                    half: int = len(str(front)) // 2
                    numbers.append(int(str(front)[:half]))
                    numbers.append(int(str(front)[half:]))
                else:
                    next_number = front * 2024
                    numbers.append(next_number)
                length -= 1
            steps -= 1

        return len(numbers)

def part2():
    file_path: str = "./inputs/11.txt"
    # dp[(number, steps)] = total length after decomposing x steps
    dp = {}
    total: int = 0
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
        numbers: List[int] = [int(number) for number in lines[0].strip().split(" ")]
        steps: int = 75

        def dfs(dp, stone, blinks):
            if blinks == 0:
                return 1
            key = (stone, blinks)
            if key in dp:
                return dp[key]

            count: int = 0
            if stone == 0:
                count = dfs(dp, 1, blinks - 1)
            elif len(str(stone)) % 2 == 0:
                half: int = len(str(stone)) // 2
                first_half: int = int(str(stone)[:half])
                second_half: int = int(str(stone)[half:])
                count = dfs(dp, first_half, blinks - 1) + dfs(dp, second_half, blinks - 1)
            else:
                count = dfs(dp, stone * 2024, blinks - 1)

            dp[key] = count

            return count

        for number in numbers:
            print(number)
            total += dfs(dp, number, steps)

    return total


if __name__ == "__main__":
    #print(part1())
    print(part2())
