from functools import reduce
from typing import List, Literal, TextIO, Tuple

from ..day import Day


class Day02(Day):
    def __init__(self):
        super().__init__("02", same_inputs_all=True)

    def __parse(self, n_dims, commands, f: TextIO):
        pos = [0] * n_dims
        for line in f:
            command, val = line.split(" ")
            val = int(val)
            commands[command](pos, val)
        return pos[0] * pos[1]

    def __shift(self, args: List[Tuple[List, int, int, Literal[-1, 1]]]):
        for pos, idx, val, dir in args:
            real_val = val if dir > 0 else -val
            pos[idx] += real_val

    def part1(self, f: TextIO):
        COMMANDS = {
            "forward": lambda pos, val: self.__shift([(pos, 0, val, 1)]),
            "down": lambda pos, val: self.__shift([(pos, 1, val, 1)]),
            "up": lambda pos, val: self.__shift([(pos, 1, val, -1)])
        }
        pos = self.__parse(2, COMMANDS, f)
        return pos

    def part2(self, f: TextIO):
        COMMANDS = {
            "down": lambda pos, val: self.__shift([(pos, 2, val, 1)]),
            "up": lambda pos, val: self.__shift([(pos, 2, val, -1)]),
            "forward": lambda pos, val:
                self.__shift([(pos, 0, val, 1),
                              (pos, 1, val * pos[2], 1)])
        }
        pos = self.__parse(3, COMMANDS, f)
        return pos
