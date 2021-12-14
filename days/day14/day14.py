from typing import TextIO
from collections import Counter, defaultdict
from copy import deepcopy

from ..day import Day


class Day14(Day):
    def __init__(self):
        super().__init__("14", same_inputs_all=True)

    def simulate(self, f: TextIO, n: int):
        template = f.readline().strip()
        f.readline()
        rules = {}
        for line in f:
            line = line.strip()
            head, _, tail = line.split()
            rules[(head[0], head[1])] = tail
        pair_counts = Counter(zip(template, template[1:]))
        for _ in range(n):
            new = deepcopy(pair_counts)
            for head, tail in rules.items():
                c = pair_counts[head]
                new[head] -= c
                n1 = (head[0], tail)
                n2 = (tail, head[1])
                new[n1] += c
                new[n2] += c
            pair_counts = new
        char_counts = defaultdict(int)
        for (c1, c2), count in pair_counts.items():
            char_counts[c1] += count
            char_counts[c2] += count
        # Characters at each index occur in two pairs each,
        # except for the first and last characters in the string.
        # This line makes the result correct when they're divided by two.
        char_counts[template[0]] += 1
        char_counts[template[-1]] += 1
        for c in char_counts:
            char_counts[c] //= 2
        most_common = Counter(char_counts).most_common()
        return most_common[0][1] - most_common[-1][1]

    def part1(self, f: TextIO):
        return self.simulate(f, 10)

    def part2(self, f: TextIO):
        return self.simulate(f, 40)
