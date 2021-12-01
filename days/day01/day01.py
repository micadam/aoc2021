from typing import TextIO
from ..day import Day
from queue import Queue


class Day01(Day):
    def __init__(self):
        super().__init__("01", same_inputs_all=True)

    def __increasing_sums(self, f: TextIO, window_width: int):
        ans = 0
        prev = 0
        last = Queue()
        for _ in range(window_width):
            num = int(f.readline())
            prev += num
            last.put(num)
        for line in f:
            num = int(line)
            next = prev + num - last.get()
            if next > prev:
                ans += 1
            prev = next
            last.put(num)
        return ans

    def part1(self, f: TextIO):
        return self.__increasing_sums(f, 1)

    def part2(self, f: TextIO):
        return self.__increasing_sums(f, 3)
