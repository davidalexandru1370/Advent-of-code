from typing import List, Tuple

def is_inside(row: int, col: int, n: int, m: int) -> bool:
    return row >= 0 and row < n and col >= 0 and col < m

def dfs(matrix: List[List[str]], row: int, col: int, n: int, m: int, word: str, count: List[int]):
    factors: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for factor in factors:
        next_row = row
        next_col = col
        for index in range(1, len(word)):
            next_row: int = next_row + factor[0]
            next_col: int = next_col + factor[1]
            if not is_inside(next_row, next_col, n, m):
                break
            if matrix[next_row][next_col] != word[index]:
                break
        else:
            count[0] = count[0] + 1
def solve_part1():
    with open("inputs/4.txt", "r") as file:
        lines: List[str] = file.readlines()
        matrix: List[List[str]] = [[str(x) for x in line.strip()] for line in lines]
        n: int = len(matrix)
        m: int = len(matrix[0])
        matrix2 = [["." for _ in range(m)] for _ in range(n)]
        word: str = "XMAS"
        count: List[int] = [0]
        for row in range(n):
            for col in range(m):
                if matrix[row][col] == 'X':
                    dfs(matrix, row, col, n, m, word, count)

    print("\n".join(["".join(row) for row in matrix2]))
    return count[0]

def solve_part2():
    with open("inputs/4.txt", "r") as file:
        lines: List[str] = file.readlines()
        matrix: List[List[str]] = [[str(x) for x in line.strip()] for line in lines]
        n: int = len(matrix)
        m: int = len(matrix[0])
        matrix2 = [["." for _ in range(m)] for _ in range(n)]
        count: int = 0
        for row in range(n):
            for col in range(m):
                if row + 2 < n and col + 2 < m:
                    left_diagonal = ''.join(sorted(matrix[row][col] + matrix[row + 1][col + 1] + matrix[row + 2][col + 2]))
                    right_diagonal = ''.join(sorted(matrix[row][col + 2] + matrix[row + 1][col + 1] + matrix[row + 2][col]))
                    if left_diagonal == right_diagonal == "AMS" and matrix[row + 1][col + 1] == 'A':
                        # matrix2[row][col] = matrix[row][col]
                        # matrix2[row][col + 2] = matrix[row][col + 2]
                        # matrix2[row + 1][col + 1] = matrix[row + 1][col + 1]
                        # matrix2[row + 2][col + 2] = matrix[row + 2][col + 2]
                        count += 1

        #print("\n".join(["".join(row) for row in matrix2]))
        return count

if __name__ == "__main__":
    # print(solve_part1())
    print(solve_part2())