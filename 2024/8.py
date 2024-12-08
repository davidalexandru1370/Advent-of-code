from typing import List, Dict, Tuple


def solve_part1() -> int:
    antinodes: int = 0
    with open("inputs/8.txt", "r") as file:
        lines = file.readlines()
        matrix: List[List[str]] = [[str(x) for x in line.strip()] for line in lines]
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        antennas: Dict[str, List[Tuple[int, int]]] = dict()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != ".":
                    if matrix[row][col] not in antennas:
                        antennas[matrix[row][col]] = []
                    antennas[matrix[row][col]].append((row, col))

        is_inside_matrix = lambda x: 0 <= x[0] < rows and 0 <= x[1] < cols
        seen = set()

        for antennas_values in antennas.values():
            if len(antennas) <= 1:
                continue
            for antenna_index1 in range(len(antennas_values)):
                for antenna_index2 in range(antenna_index1 + 1, len(antennas_values)):
                    antenna1 = antennas_values[antenna_index1]
                    antenna2 = antennas_values[antenna_index2]
                    min_antenna = min(antenna1, antenna2)
                    max_antenna = max(antenna1, antenna2)
                    distance = (max_antenna[0] - min_antenna[0], max_antenna[1] - min_antenna[1])
                    antinode_min = (max_antenna[0] - 2 * distance[0], max_antenna[1] - 1 * distance[1])
                    antinode_max = (min_antenna[0] + 2 * distance[0], min_antenna[1] + 2 * distance[1])
                    factor: int = 2
                    while is_inside_matrix(antinode_min):
                        antinodes += 1
                        # seen.add(antinode_min)
                        matrix[antinode_min[0]][antinode_min[1]] = '#'
                        factor += 1
                        antinode_min = (max_antenna[0] - factor * distance[0], max_antenna[1] - factor * distance[1])
                    factor = 2
                    while is_inside_matrix(antinode_max):
                        antinodes += 1
                        matrix[antinode_max[0]][antinode_max[1]] = '#'
                        factor += 1
                        antinode_max = (min_antenna[0] + factor * distance[0], min_antenna[1] + factor * distance[1])

        print("\n".join(["".join(x) for x in matrix]))
    return antinodes


def solve_part2():
    antinodes: int = 0
    with open("inputs/8.txt", "r") as file:
        lines = file.readlines()
        matrix: List[List[str]] = [[str(x) for x in line.strip()] for line in lines]
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        antennas: Dict[str, List[Tuple[int, int]]] = dict()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != ".":
                    if matrix[row][col] not in antennas:
                        antennas[matrix[row][col]] = []
                    antennas[matrix[row][col]].append((row, col))

        is_inside_matrix = lambda x: 0 <= x[0] < rows and 0 <= x[1] < cols
        seen = set()

        for antennas_values in antennas.values():
            if len(antennas) <= 1:
                continue
            for antenna_index1 in range(len(antennas_values)):
                for antenna_index2 in range(antenna_index1 + 1, len(antennas_values)):
                    antenna1 = antennas_values[antenna_index1]
                    antenna2 = antennas_values[antenna_index2]
                    min_antenna = min(antenna1, antenna2)
                    max_antenna = max(antenna1, antenna2)
                    distance = (max_antenna[0] - min_antenna[0], max_antenna[1] - min_antenna[1])
                    antinode_min = (max_antenna[0] - 1 * distance[0], max_antenna[1] - 1 * distance[1])
                    antinode_max = (min_antenna[0] + 1 * distance[0], min_antenna[1] + 1 * distance[1])
                    factor: int = 1
                    while is_inside_matrix(antinode_min):
                        if antinode_min not in seen and matrix[antinode_min[0]][antinode_min[1]] in [".", "#"]:
                            antinodes += 1
                            seen.add(antinode_min)
                            matrix[antinode_min[0]][antinode_min[1]] = '#'
                        factor += 1
                        antinode_min = (max_antenna[0] - factor * distance[0], max_antenna[1] - factor * distance[1])
                    factor = 1
                    while is_inside_matrix(antinode_max):
                        if antinode_max not in seen and matrix[antinode_max[0]][antinode_max[1]] in [".", "#"]:
                            antinodes += 1
                            seen.add(antinode_max)
                            matrix[antinode_max[0]][antinode_max[1]] = '#'
                        factor += 1
                        antinode_max = (min_antenna[0] + factor * distance[0], min_antenna[1] + factor * distance[1])
        #print("\n".join(["".join(x) for x in matrix]))
    return antinodes + sum([len(a) for a in antennas.values()])


if __name__ == "__main__":
    # print(solve_part1())
    print(solve_part2())
