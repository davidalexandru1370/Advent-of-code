from typing import List, Tuple, Dict, Set


def is_inside(row: int, column: int, rows: int, columns: int) -> bool:
    return 0 <= row < rows and 0 <= column < columns


def dfs(row: int, column: int, next_pos: int, grid: List[List[int]], found: List[int], seen: Set[Tuple[int, int]]):
    if grid[row][column] == 9 or next_pos == 10:
        key = (row, column)
        if key not in seen:
            found[0] += 1
            seen.add(key)

    directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows: int = len(grid)
    columns: int = len(grid[0])

    for direction in directions:
        next_row = row + direction[0]
        next_col = column + direction[1]
        if is_inside(next_row, next_col, rows, columns) and grid[next_row][next_col] == next_pos:
            dfs(next_row, next_col, next_pos + 1, grid, found, seen)


def solve_part1():
    file_path: str = "./inputs/10.txt"
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
        grid: List[List[int]] = [[int(l) for l in line.strip()] for line in lines]
        rows: int = len(grid)
        columns: int = len(grid[0])
        trails: Dict[Tuple[int, int], int] = {}
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0:
                    found = [0]
                    dfs(row, column, 1, grid, found, set())
                    trails[(row, column)] = found[0]

    print(sum(trails.values()))

def dfs(row: int, column: int, next_pos: int, grid: List[List[int]], found: List[int]):
    if grid[row][column] == 9 or next_pos == 10:
        found[0] += 1

    directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows: int = len(grid)
    columns: int = len(grid[0])

    for direction in directions:
        next_row = row + direction[0]
        next_col = column + direction[1]
        if is_inside(next_row, next_col, rows, columns) and grid[next_row][next_col] == next_pos:
            dfs(next_row, next_col, next_pos + 1, grid, found)

def solve_part2():
    file_path: str = "./inputs/10.txt"
    with open(file_path, "r") as f:
        lines: List[str] = f.readlines()
        grid: List[List[int]] = [[int(l) for l in line.strip()] for line in lines]
        rows: int = len(grid)
        columns: int = len(grid[0])
        trails: Dict[Tuple[int, int], int] = {}
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0:
                    found = [0]
                    dfs(row, column, 1, grid, found)
                    trails[(row, column)] = found[0]

    print(sum(trails.values()))


if __name__ == "__main__":
    # solve_part1()
    solve_part2()
