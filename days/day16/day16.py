from typing import TextIO
from functools import reduce
from math import inf

from ..day import Day

VERSION_LEN = 3
TYPE_ID_LEN = 3
LGT_TYPE_LEN = 1
MORE_TO_READ_LEN = 1
SEGMENT_LEN = 4
TOTAL_LENGTH_LEN = 15
NUM_OF_PACKETS_LEN = 11


class Input:
    def __init__(self, binary_input: str):
        self.binary_input = binary_input
        self.idx = 0

    def read_bits(self, lgt):
        self.idx += lgt
        val = int(self.binary_input[:lgt], base=2)
        self.binary_input = self.binary_input[lgt:]
        return val


class Day16(Day):
    def __init__(self):
        super().__init__("16", same_inputs_all=True)

    def __parse_literal(self, inp: Input):
        more_to_read = True
        val = 0
        while more_to_read:
            val *= 16
            more_to_read = inp.read_bits(MORE_TO_READ_LEN)
            val += inp.read_bits(SEGMENT_LEN)
        return val

    def __get_subpackets_total_len(self, inp):
        total_length = inp.read_bits(TOTAL_LENGTH_LEN)
        idx = inp.idx
        while inp.idx - idx != total_length:
            yield

    def __get_subpackets_num_subpackets(self, inp):
        num_of_packets = inp.read_bits(NUM_OF_PACKETS_LEN)
        for _ in range(num_of_packets):
            yield

    LITERAL_TYPE = 4

    def __sum_version_numbers(self, inp: Input):
        ver = inp.read_bits(VERSION_LEN)
        typ = inp.read_bits(TYPE_ID_LEN)
        if typ == self.LITERAL_TYPE:
            self.__parse_literal(inp)
            return ver
        lgt_type = inp.read_bits(LGT_TYPE_LEN)
        subpackets_iter = self.__get_subpackets_num_subpackets(inp) \
            if lgt_type \
            else self.__get_subpackets_total_len(inp)
        for _ in subpackets_iter:
            ver += self.__sum_version_numbers(inp)
        return ver

    EXPRESSION_TYPES = {
        0: (int.__add__, 0),
        1: (int.__mul__, 1),
        2: (min, inf),
        3: (max, -inf),
    }

    COMPARABLE_TYPES = {
        5: int.__gt__,
        6: int.__lt__,
        7: int.__eq__,
    }

    def __evaluate(self, inp: Input):
        _ = inp.read_bits(VERSION_LEN)
        typ = inp.read_bits(TYPE_ID_LEN)
        if typ == self.LITERAL_TYPE:
            return self.__parse_literal(inp)
        lgt_type = inp.read_bits(LGT_TYPE_LEN)
        subpackets_iter = self.__get_subpackets_num_subpackets(inp) \
            if lgt_type \
            else self.__get_subpackets_total_len(inp)
        if typ in self.EXPRESSION_TYPES:
            vals = []
            for _ in subpackets_iter:
                vals.append(self.__evaluate(inp))
            func, init = self.EXPRESSION_TYPES[typ]
            return reduce(func, vals, init)
        elif typ in self.COMPARABLE_TYPES:
            # This type always has 2 subpackets.
            # Just call the iterator once to consume the length segment.
            next(subpackets_iter)
            x = self.__evaluate(inp)
            y = self.__evaluate(inp)
            return self.COMPARABLE_TYPES[typ](x, y)

    def __get_input(self, f: TextIO):
        bin_input = "".join(map(lambda c: bin(int(c, base=16))[2:].zfill(4),
                                f.read().strip()))
        return Input(bin_input)

    def part1(self, f: TextIO):
        inp = self.__get_input(f)
        return self.__sum_version_numbers(inp)

    def part2(self, f: TextIO):
        inp = self.__get_input(f)
        return self.__evaluate(inp)
