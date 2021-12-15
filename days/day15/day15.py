from queue import PriorityQueue
from typing import TextIO

from ..day import Day

DIRS = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def generate_neighbours(y, x, Y, X):
    for dy, dx in DIRS:
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            yield ny, nx


class Day15(Day):
    def __init__(self):
        super().__init__("15", same_inputs_all=True)

    def __solve(self, m):
        q = PriorityQueue()
        Y = len(m)
        X = len(m[0])
        # total cost, coordinates
        q.put((0, (0, 0)))
        visited = [[False for _ in range(X)] for _ in range(Y)]
        while q.qsize():
            (cost, (y, x)) = q.get()
            for ny, nx in generate_neighbours(y, x, Y, X):
                if visited[ny][nx]:
                    continue
                new_cost = cost + m[ny][nx]
                if (ny, nx) == (Y - 1, X - 1):
                    return new_cost
                visited[ny][nx] = True
                q.put((new_cost, (ny, nx)))
        raise RuntimeError("No path found")

    def part1(self, f: TextIO):
        m = [list(map(int, line.strip())) for line in f]
        return self.__solve(m)

    def part2(self, f: TextIO):
        m = [list(map(int, line.strip())) for line in f]
        Y = len(m)
        X = len(m[0])
        bm = [[None for _ in range(Y * 5)] for _ in range(X * 5)]
        for y in range(len(bm)):
            for x in range(len(bm[y])):
                val = (m[y % Y][x % X] + y // Y + x // X)
                bm[y][x] = val % 10 + val // 10

        return self.__solve(bm)
