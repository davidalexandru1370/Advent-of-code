from typing import List, Set, Tuple, Deque, Callable, Dict
from collections import deque

#area, perimeter
def bfs(rows: int, cols: int, grid: List[List[str]], visited: Set[Tuple[int, int]], i: int, j: int) -> Tuple[int, int]:
    is_inside: Callable[[int, int], bool] = lambda x, y: x >= 0 and x < rows and y >= 0 and y < cols
    queue: Deque[Tuple[int, int]] = deque()
    key: Tuple[int, int] = (i, j)
    queue.append(key)
    visited.add(key)
    area: int = 0
    perimeter: int = 0
    neighbours: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while len(queue) > 0:
        x, y = queue.popleft()
        for xx, yy in neighbours:
            new_xx: int = x + xx
            new_yy: int = y + yy
            if not is_inside(new_xx, new_yy) or grid[new_xx][new_yy] != grid[x][y]:
                perimeter += 1
        area += 1
        for dx, dy in neighbours:
            new_x: int = x + dx
            new_y: int = y + dy
            key: Tuple[int, int] = (new_x, new_y)
            if key not in visited:
                if is_inside(new_x, new_y) and grid[new_x][new_y] == grid[x][y]:
                    visited.add(key)
                    queue.append(key)
    
    return (area, perimeter)


def traverse_contour(rows: int, cols: int, grid: List[List[str]], visited: Set[Tuple[int, int]], i: int, j: int) -> Tuple[int, int]:
    is_inside: Callable[[int, int], bool] = lambda x, y: x >= 0 and x < rows and y >= 0 and y < cols
    queue: Deque[Tuple[int, int]] = deque()
    key: Tuple[int, int] = (i, j)
    queue.append(key)
    visited.add(key)
    area: int = 0
    sides: int = 0
    perimeter: int = 0
    contour: Dict[Tuple[int, int], Set[Tuple[int, int]]] = {}
    neighbours: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while len(queue) > 0:
        x, y = queue.popleft()
        for xx, yy in neighbours:
            new_xx: int = x + xx
            new_yy: int = y + yy
            if not is_inside(new_xx, new_yy) or grid[new_xx][new_yy] != grid[x][y]:
                perimeter += 1
                if (xx, yy) not in contour:
                    contour[(xx, yy)] = set()
                contour[(xx, yy)].add((x, y))

        area += 1
        for dx, dy in neighbours:
            new_x: int = x + dx
            new_y: int = y + dy
            key: Tuple[int, int] = (new_x, new_y)
            if key not in visited:
                if is_inside(new_x, new_y) and grid[new_x][new_y] == grid[x][y]:
                    visited.add(key)
                    queue.append(key)

    for k, vs in contour.items():
        visited_contour: Set[Tuple[int, int]] = set()
        for x, y in vs:
            if (x, y) not in visited_contour:
                #visited_contour.add((x, y))
                sides += 1
                queue = deque([(x, y)])
                while len(queue) > 0:
                    frontx, fronty = queue.popleft()
                    if (frontx, fronty) in visited_contour:
                        continue
                    visited_contour.add((frontx, fronty))
                    for dr, dc in neighbours:
                        new_x: int = frontx + dr
                        new_y: int = fronty + dc
                        if (new_x, new_y) in vs:
                            queue.append((new_x, new_y))
    
    return (area, sides)



def solve_part_1():
    file_name:str = "inputs/12.txt"
    with  open(file_name, 'r') as f:
        grid: List[List[str]] = []
        for line in f.readlines():
            grid.append([x for x in line.strip()])
        visited: Set[Tuple[int, int]] = set()
        print(grid)
        total_price: int = 0
        rows: int = len(grid)
        cols: int = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                key: Tuple[int, int] = (i, j)
                if key not in visited:
                    area, perimeter = bfs(rows, cols, grid, visited, i, j)
                    print(f"Area: {area}, Perimeter: {perimeter}")
                    total_price += area * perimeter
        print(f"Total price: {total_price}")

def solve_part_2():
    file_name:str = "inputs/12.txt"
    with  open(file_name, 'r') as f:
        grid: List[List[str]] = []
        for line in f.readlines():
            grid.append([x for x in line.strip()])
        visited: Set[Tuple[int, int]] = set()
        print(grid)
        total_price: int = 0
        rows: int = len(grid)
        cols: int = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                key: Tuple[int, int] = (i, j)
                if key not in visited:
                    area, sides = traverse_contour(rows, cols, grid, visited, i, j)
                    print(f"Area: {area}, Sides: {sides}")
                    total_price += area * sides
        print(f"Total price: {total_price}")

if __name__ == "__main__":
    # solve_part_1()
    solve_part_2()