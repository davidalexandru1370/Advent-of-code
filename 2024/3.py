from typing import List
import re

def solve_part1():
    filename:str = "inputs/3.txt"
    with open(filename, "r") as f:
        lines: List[str] = f.readlines()
        mul_pattern = r"mul\(\d+,\d+\)"
        result: int = 0
        for line in lines:
            all_found = re.findall(mul_pattern, line)
            for pattern in all_found:
                numbers = [int(x) for x in re.findall("\d+", pattern)]
                result += numbers[0] * numbers[1]

        return result
            

def solve_part2():
    filename: str = "inputs/3.txt"
    with open(filename, "r") as f:
        lines: List[str] = f.readlines()
        mul_pattern = r"mul\(\d+,\d+\)|do\(\)|dont\(\)"
        result: int = 0
        do: bool = True 
        for line in lines:
            line = line.replace("'", "")
            all_found = re.findall(mul_pattern, line)
            for pattern in all_found:
                if pattern == "do()":
                    do = True
                elif pattern == "dont()":
                    do = False
                elif do == True:
                    a, b = map(int, pattern[4:-1].split(","))
                    result += a * b
    return result
                


if __name__ == "__main__":
    #print(solve_part1())
    print(solve_part2())
