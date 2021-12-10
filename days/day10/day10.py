from math import ceil, floor
from typing import List, TextIO
from queue import PriorityQueue, Queue

from ..day import Day

CHUNKS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
VALS_1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
VALS_2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


class Day10(Day):
    def __init__(self):
        super().__init__("10", same_inputs_all=True)

    def part1(self, f: TextIO):
        ans = 0
        for line in f:
            stack = []
            for c in line.strip():
                if c in CHUNKS:
                    stack.append(c)
                else:
                    first = stack.pop()
                    if CHUNKS[first] != c:
                        ans += VALS_1[c]
                        break
        return ans

    def part2(self, f: TextIO):
        scores = []
        for line in f:
            stack = []
            ok_to_complete = True
            for c in line.strip():
                if c in CHUNKS:
                    stack.append(c)
                else:
                    first = stack.pop()
                    if CHUNKS[first] != c:
                        ok_to_complete = False
                        break
            if not ok_to_complete:
                continue
            score = 0
            for c in reversed(stack):
                score *= 5
                score += VALS_2[c]
            scores.append(score)
        return sorted(scores)[len(scores) // 2]
