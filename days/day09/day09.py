from math import ceil, floor
from typing import List, TextIO
from queue import PriorityQueue, Queue

from ..day import Day

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Day09(Day):
    def __init__(self):
        super().__init__("09", same_inputs_all=True)

    def __solve(self, f):
        return 0

    def part1(self, f: TextIO):
        inp = [list(map(int, line.replace("\n", ""))) for line in f]
        Y = len(inp)
        X = len(inp[0])
        ans = 0
        for y in range(Y):
            for x in range(X):
                lowest = True
                val = inp[y][x]
                for dy, dx in DIRS:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < Y and 0 <= nx < X and inp[ny][nx] <= val:
                        lowest = False
                        break
                if lowest:
                    ans += val + 1
        return ans

    def part2(self, f: TextIO):
        inp = [list(map(int, line.replace("\n", ""))) for line in f]
        Y = len(inp)
        X = len(inp[0])
        basin_ids = [[None] * X for _ in range(Y)]
        next_basin_id = 0
        for y in range(Y):
            for x in range(X):
                # Lord forgive me
                if inp[y][x] == 9 or basin_ids[y][x] is not None:
                    continue
                basin_id = next_basin_id
                next_basin_id += 1
                to_visit = Queue()
                to_visit.put((y, x))
                while to_visit.qsize():
                    my, mx = to_visit.get()
                    basin_ids[my][mx] = basin_id
                    for dy, dx in DIRS:
                        ny, nx = my + dy, mx + dx
                        if 0 <= ny < Y and 0 <= nx < X \
                                and inp[ny][nx] != 9 \
                                and basin_ids[ny][nx] is None:
                            to_visit.put((ny, nx))
        biggest = PriorityQueue()
        for i in range(next_basin_id):
            biggest.put(-sum(row.count(i) for row in basin_ids))
        ans = 1
        for _ in range(3):
            ans *= -biggest.get()
        return ans
