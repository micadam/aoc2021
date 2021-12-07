from typing import Text, TextIO
from collections import defaultdict

from ..day import Day


class Day06(Day):
    def __init__(self):
        super().__init__("06", same_inputs_all=True)

    def __solve(self, f, days):
        fish = list(map(int, f.read().split(",")))
        fish_counters = defaultdict(int)
        for f in fish:
            fish_counters[f] += 1
        for d in range(days):
            new_fish_counters = defaultdict(int)
            for i in range(9):
                if i == 8:
                    new_fish_counters[i] = fish_counters[0]
                elif i == 6:
                    new_fish_counters[i] = fish_counters[0] + fish_counters[7]
                else:
                    new_fish_counters[i] = fish_counters[i + 1]
            fish_counters = new_fish_counters
        return sum(fish_counters.values())

    def part1(self, f: TextIO):
        return self.__solve(f, 80)

    def part2(self, f: TextIO):
        return self.__solve(f, 256)
