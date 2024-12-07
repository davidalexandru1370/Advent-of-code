from typing import Tuple, Set, List


def rotate_90(direction: Tuple[int, int]) -> Tuple[int, int]:
    next_direction = {
        (-1, 0): (0, 1),
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0)
    }

    return next_direction[direction]


def get_direction_name(direction: Tuple[int, int]) -> str:
    if direction == (-1, 0):
        return "U"
    elif direction == (0, 1):
        return "R"
    elif direction == (1, 0):
        return "D"
    elif direction == (0, -1):
        return "L"


def solve_part1():
    with open("inputs/6.txt", "r") as file:
        lines = file.readlines()
        count: int = 0
        matrix: List[List[str]] = [[str(x) for x in line.strip()] for line in lines]
        current_direction = (-1, 0)
        current_position: Tuple[int, int] = next(
            (i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == '^')
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        visited: Set[Tuple[int, int]] = set()
        visited.add(current_position)
        moves_left: bool = True
        while moves_left:
            next_row: int = current_position[0] + current_direction[0]
            next_col: int = current_position[1] + current_direction[1]
            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                moves_left = False
                break

            if matrix[next_row][next_col] == "#":
                current_direction = rotate_90(current_direction)
                continue

            current_position = (next_row, next_col)

            if (next_row, next_col) not in visited:
                matrix[next_row][next_col] = 'X'
                count += 1
            visited.add(current_position)

    return len(visited)


def is_in_loop(matrix: List[List[str]], start_position: Tuple[int, int]) -> bool:
    seen = set()
    current_direction: Tuple[int, int] = (-1, 0)
    seen.add((start_position[0], start_position[1], get_direction_name(current_direction)))
    in_loop: bool = False
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    while True:
        next_row: int = start_position[0] + current_direction[0]
        next_col: int = start_position[1] + current_direction[1]
        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
            break

        if matrix[next_row][next_col] == "#":
            current_direction = rotate_90(current_direction)
            continue

        direction_name: str = get_direction_name(current_direction)
        start_position = (next_row, next_col)
        if (next_row, next_col, direction_name) not in seen:
            seen.add((next_row, next_col, direction_name))
        else:
            in_loop = True
            break

    return in_loop


def solve_part2():
    with open("inputs/6.txt", "r") as file:
        lines = file.readlines()
        count: int = 0
        matrix: List[List[str]] = [[str(x) for x in line.strip()] for line in lines]
        current_direction = (-1, 0)
        start_position: Tuple[int, int] = next(
            (i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == '^')
        current_position: Tuple[int, int] = start_position
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        visited: Set[Tuple[int, int]] = set()
        visited.add(current_position)
        moves_left: bool = True
        while moves_left:
            next_row: int = current_position[0] + current_direction[0]
            next_col: int = current_position[1] + current_direction[1]
            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                break

            if matrix[next_row][next_col] == "#":
                current_direction = rotate_90(current_direction)
                continue

            current_position = (next_row, next_col)

            if (next_row, next_col) not in visited:
                count += 1
            visited.add(current_position)

        ways: int = 0

        for row, col in list(visited):
            if (row, col) != start_position:
                matrix[row][col] = '#'
                if is_in_loop(matrix, (start_position[0], start_position[1])) == True:
                    ways += 1
                matrix[row][col] = '.'
        return ways


if __name__ == "__main__":
    # print(solve_part1())
    print(solve_part2())
