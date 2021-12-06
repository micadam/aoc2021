from typing import Text, TextIO
from collections import defaultdict

from ..day import Day


class Day05(Day):
    def __init__(self):
        super().__init__("05", same_inputs_all=True)

    def __solve(self, f: TextIO, diag=False):
        points = defaultdict(int)
        for line in f:
            [x1, y1, x2, y2] = map(int,
                                   line.replace(" -> ", ",").split(","))

            x_step = 1 if x2 > x1 else -1
            y_step = 1 if y2 > y1 else -1
            if x1 == x2:
                for y in range(y1, y2 + y_step, y_step):
                    points[(x1, y)] += 1
            elif y1 == y2:
                for x in range(x1, x2 + x_step, x_step):
                    points[(x, y1)] += 1
            elif diag:
                for x, y in zip(range(x1, x2 + x_step, x_step),
                                range(y1, y2 + y_step, y_step)):
                    points[(x, y)] += 1
        return sum(1 for val in points.values() if val > 1)

    def part1(self, f: TextIO):
        return self.__solve(f)

    def part2(self, f: TextIO):
        return self.__solve(f, True)
