from typing import TextIO

from ..day import Day


class Day03(Day):
    def __init__(self):
        super().__init__("03", same_inputs_all=True)

    def part1(self, f: TextIO):
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
        lgt = len(lines[0])
        gamma = 0
        epsilon = 0
        for i in range(lgt):
            num_lines = len(lines)
            gamma *= 2
            epsilon *= 2
            count_ones = len([line for line in lines
                             if line[i] == '1'])
            if count_ones > num_lines / 2:
                gamma += 1
            else:
                epsilon += 1
        print(gamma)
        print(epsilon)
        return gamma * epsilon

    def part2(self, f: TextIO):
        lines = f.readlines()
        lines = [lines[:-1] for line in lines]
        lgt = len(lines[0])
        lines_oxygen = lines.copy()
        lines_co2 = lines.copy()
        for i in range(lgt):
            if len(lines_oxygen) > 1:
                num_lines = len(lines_oxygen)
                count_ones = [li[i] for li in lines_oxygen].count("1")
                most_common = "1" \
                    if count_ones >= num_lines / 2 \
                    else "0"
                lines_oxygen = [li for li in lines_oxygen
                                if li[i] == most_common]
            if len(lines_co2) > 1:
                num_lines = len(lines_co2)
                count_zeros = [li[i] for li in lines_co2].count("0")
                least_common = "0" \
                    if count_zeros <= num_lines / 2 \
                    else "1"
                lines_co2 = [li for li in lines_co2
                             if li[i] == least_common]
        return int(lines_oxygen[0], 2) * int(lines_co2[0], 2)
