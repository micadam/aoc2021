from math import ceil, floor
from typing import Text, TextIO

from ..day import Day


class Day07(Day):
    def __init__(self):
        super().__init__("07", same_inputs_all=True)

    def part1(self, f: TextIO):
        points = sorted(list(map(int, f.read().split(","))))
        mid = int(len(points) / 2) \
            if len(points) % 2 \
            else int((len(points) + 1) / 2)
        return sum(abs(p - points[mid]) for p in points)

    def __dist2(self, d):
        return int(d * (d + 1) / 2)

    def part2(self, f: TextIO):
        points = list(map(int, f.read().split(",")))
        mean = sum(points) / len(points)
        options = [floor(mean), ceil(mean)]
        return min(sum(self.__dist2(abs(p - opt))
                       for p in points)
                   for opt in options)
