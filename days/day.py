from typing import TextIO
from timeit import default_timer as timer

class Day:
    def __init__(self, number, same_inputs_all=False,
                 same_inputs_test=False, same_inputs_actual=False):
        self.number = number
        same_inputs_actual = same_inputs_actual or same_inputs_all
        same_inputs_test = same_inputs_test or same_inputs_all
        self.in1 = f"input/{number}_1.in"
        self.in2 = self.in1 if same_inputs_actual else \
            f"input/{number}_2.in"
        self.in1_test = f"input/{number}_1_test.in"
        self.in2_test = self.in1_test if same_inputs_test else \
            f"input/{number}_2_test.in"

    def part1(f: TextIO, self):
        raise NotImplementedError

    def part2(f: TextIO, self):
        raise NotImplementedError

    def solve(self, test=False):
        if not test:
            in1 = self.in1
            in2 = self.in2
        else:
            in1 = self.in1_test
            in2 = self.in2_test
        print(f"Advent Of Code 2021, day {self.number}")
        with open(in1) as f1:
            start = timer()
            ans_part1 = self.part1(f1)
            time = timer() - start
        print(f"Part 1: {ans_part1}, time: {time} s")
        with open(in2) as f2:
            start = timer()
            ans_part2 = self.part2(f2)
            time = timer() - start
        print(f"Part 2: {ans_part2}, time: {time} s")

    def __call__(self, test):
        self.solve(test)
