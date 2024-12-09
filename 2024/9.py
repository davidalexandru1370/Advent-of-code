import heapq
from typing import List, Tuple

def solve_part1() -> int:
    with open("inputs/9.txt", "r") as file:
        lines = file.readlines()
        disk_map: List[List[int, int, int]] = []
        line: str = lines[0]
        index: int = 0
        id: int = 0
        while index < len(line):
            occupied: int = int(line[index])
            free_space: int = 0
            if index + 1 < len(line):
                free_space = int(line[index + 1])
            disk_map.append([occupied, free_space, id])
            id += 1
            index += 2

        right: int = len(disk_map) - 1
        left: int = 0
        index = 0
        checksum: int = 0
        while left <= right:
            while disk_map[left][0] > 0:
                checksum += index * disk_map[left][2]
                index += 1
                disk_map[left][0] -= 1
            while disk_map[left][1] > 0 and disk_map[right][0] > 0:
                checksum += index * disk_map[right][2]

                disk_map[right][0] -= 1
                disk_map[left][1] -= 1
                index += 1
                while disk_map[right][0] == 0 and right >= 0:
                    right -= 1
            left += 1
        return checksum

class Memory:
    def __init__(self, id: int, memory: int, free_space: int, index: int):
        self.id = id
        self.memory = memory
        self.free_space = free_space
        self.index = index
        self.before_free_zone = 0
        self.free_spaces = []

    def fill_free_spaces(self, amount, id):
        self.free_space -= amount
        self.free_spaces.extend([id for _ in range(amount)])


    def __str__(self):
        return f'id = {self.id} memory = {self.memory} free_space = {self.free_space} free_spaces = {self.free_spaces}'

def solve_part2() -> int:
    with open("inputs/9.txt", "r") as file:
        line: str = file.readline()
        checksum: int = 0
        disk_map = []
        index: int = 0
        id: int = 0
        free_space_heap: List[Tuple[int, 'Memory']] = []
        ram = []
        while index < len(line):
            occupied: int = int(line[index])
            free_space: int = 0 if index + 1 >= len(line) else int(line[index + 1])
            memory: "Memory" = Memory(id, occupied, free_space, index)
            ram.append(memory)
            free_space_heap.append((index, memory))
            id += 1
            index += 2

        heapq.heapify(free_space_heap)

        left: int = 0
        right: int = len(ram) - 1

        while right >= 0:
            if ram[right].memory > 0:
                popped_items = []
                while len(free_space_heap) > 0 and free_space_heap[0][1].free_space < ram[right].memory:
                    popped_items.append(heapq.heappop(free_space_heap))

                if len(free_space_heap) > 0 and free_space_heap[0][1].free_space >= ram[right].memory and free_space_heap[0][1].index <= right:
                    top = heapq.heappop(free_space_heap)
                    memory = top[1]
                    if len(ram[right].free_spaces) > 0:
                        ram[right].before_free_zone += ram[right].memory
                    else:
                        ram[right].free_space += ram[right].memory
                    memory.fill_free_spaces(ram[right].memory, ram[right].id)
                    ram[right].memory = 0
                    heapq.heappush(free_space_heap, (top[0], memory))

                for item in popped_items:
                    heapq.heappush(free_space_heap, item)

            right -= 1

        index: int = 0
        checksum: int = 0
        while left < len(ram):
            # print(str(ram[left]))
            while ram[left].memory > 0:
                checksum += ram[left].id * index
                #pattern += str(ram[left].id)
                index += 1
                ram[left].memory -= 1
            while ram[left].before_free_zone > 0:
                index += 1
                #pattern +="."
                ram[left].before_free_zone -= 1
            for it in ram[left].free_spaces:
                #pattern += str(it)
                checksum += it * index
                index += 1
            while ram[left].free_space > 0:
                #pattern += "."
                index += 1
                ram[left].free_space -= 1
            left += 1
    #print(pattern)
    return checksum

if __name__ == "__main__":
    #print(solve_part1())
    print(solve_part2())