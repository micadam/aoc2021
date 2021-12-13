from typing import Set, TextIO, Tuple
from copy import copy

from ..day import Day


class Day13(Day):
    def __init__(self):
        super().__init__("13", same_inputs_all=True)

    def __visualize(self, dots):
        max_x = max(dot[0] for dot in dots)
        max_y = max(dot[1] for dot in dots)
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                print("#" if (x, y) in dots else ".", end="")
            print()

    def __fold(self, f: TextIO, max_folds: int, vizualize=False):
        dots: Set[Tuple[int, int]] = set()
        for line in f:
            line = line.strip()
            if not line:
                break
            x, y = map(int, line.split(","))
            dots.add((x, y))
        for line in f.readlines()[:max_folds]:
            axis, val = line.split()[2].split("=")
            val = int(val)
            if axis == "x":
                idx = 0
            elif axis == "y":
                idx = 1
            else:
                raise ValueError("reee")
            new_dots = set()
            for dot in dots:
                if dot[idx] < val:
                    new_dots.add(dot)
                elif dot[idx] > val:
                    offset = dot[idx] - val
                    new_dot = tuple(val - offset if i == idx else item
                                    for i, item in enumerate(dot))
                    new_dots.add(new_dot)
            dots = new_dots
        if vizualize:
            self.__visualize(dots)
        return len(dots)

    def part1(self, f: TextIO):
        return self.__fold(f, 1)

    def part2(self, f: TextIO):
        return self.__fold(f, int(2e10), vizualize=True)
