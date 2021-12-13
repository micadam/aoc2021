from typing import TextIO
from queue import Queue

from ..day import Day

DIRS = [
    (0, 1), (-1, 1), (-1, 0), (-1, -1),
    (0, -1), (1, -1), (1, 0), (1, 1)
]


def generate_all_coords(Y, X):
    for y in range(Y):
        for x in range(X):
            yield (y, x)


def generate_neighbours(y, x, Y, X):
    for dy, dx in DIRS:
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            yield (ny, nx)


class Day11(Day):
    def __init__(self):
        super().__init__("11", same_inputs_all=True)

    def simulate(self, f: TextIO, n: int):
        octs = []
        for line in f:
            octs.append(list(map(int, line.strip())))
        Y = len(octs)
        X = len(octs[0])
        ans1 = 0
        ans2 = None
        lgt = sum(len(oct) for oct in octs)
        for i in range(n):
            popped = set()
            to_pop = Queue()
            for y, x in generate_all_coords(Y, X):
                octs[y][x] += 1
                if octs[y][x] > 9:
                    to_pop.put((y, x))
                    popped.add((y, x))
            while to_pop.qsize():
                y, x = to_pop.get()
                for ny, nx in generate_neighbours(y, x, Y, X):
                    if (ny, nx) in popped:
                        continue
                    octs[ny][nx] += 1
                    if octs[ny][nx] > 9:
                        to_pop.put((ny, nx))
                        popped.add((ny, nx))
            for y, x in popped:
                octs[y][x] = 0
            # bleh
            if n > 100 and len(popped) == lgt:
                ans2 = i + 1
                break
            ans1 += len(popped)
        return ans1, ans2

    def part1(self, f: TextIO):
        return self.simulate(f, 100)[0]

    def part2(self, f: TextIO):
        return self.simulate(f, int(2e10))[1]
