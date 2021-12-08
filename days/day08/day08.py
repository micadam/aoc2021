from math import ceil, floor
from typing import List, TextIO

from ..day import Day


class Day08(Day):
    def __init__(self):
        super().__init__("08", same_inputs_all=True)

    def __solve(self, f):
        return 0

    def part1(self, f: TextIO):
        ans = 0
        for line in f:
            segments = line.split()
            mid = segments.index("|")
            outs = segments[mid + 1:]
            ans += sum(1 for out in outs if len(out) in [2, 3, 4, 7])
        return ans

    def __get_digits_by_length(self, ins, length: int) -> List[set]:
        return [i for i in ins if len(i) == length]

    def __filter_intersection_len(self, ins, comp, length):
        return next(filter(lambda i: len(i.intersection(comp)) == length, ins))

    def part2(self, f: TextIO):
        ans = 0
        for line in f:
            segments = line.split()
            mid = segments.index("|")
            digits = [None] * 10
            ins = list(map(set, segments[:mid]))
            outs = list(map(set, segments[mid + 1:]))
            # The simple digits
            digits[1] = self.__get_digits_by_length(ins, 2)[0]
            digits[4] = self.__get_digits_by_length(ins, 4)[0]
            digits[7] = self.__get_digits_by_length(ins, 3)[0]
            digits[8] = self.__get_digits_by_length(ins, 7)[0]
            # Two Three Five
            len5 = self.__get_digits_by_length(ins, 5)
            # Three is the only one of these that has
            # the right edge (a.k.a. One) full
            digits[3] = self.__filter_intersection_len(len5, digits[1], 2)
            len5.remove(digits[3])
            # Aligning Three and Four on top of each other yields Nine
            digits[9] = digits[3].union(digits[4])
            # Zero Six Nine
            len6 = self.__get_digits_by_length(ins, 6)
            len6.remove(digits[9])
            # Similar logic to Three above, right edge full
            digits[0] = self.__filter_intersection_len(len6, digits[1], 2)
            len6.remove(digits[0])
            # Last one left
            digits[6] = len6[0]
            # Only Two and Five left, and they have
            # different-sized intersections with 6
            digits[2] = self.__filter_intersection_len(len5, digits[6], 4)
            len5.remove(digits[2])
            digits[5] = len5[0]
            # Decode the outputs
            an = 0
            for o in outs:
                an *= 10
                an += digits.index(o)
            ans += an
        return ans
