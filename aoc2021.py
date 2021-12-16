import sys
from days.day01 import Day01
from days.day02 import Day02
from days.day03 import Day03
from days.day04 import Day04
from days.day05 import Day05
from days.day06 import Day06
from days.day07 import Day07
from days.day08 import Day08
from days.day09 import Day09
from days.day10 import Day10
from days.day11 import Day11
from days.day12 import Day12
from days.day13 import Day13
from days.day14 import Day14
from days.day15 import Day15
from days.day16 import Day16

DAYS = {
    1: Day01(),
    2: Day02(),
    3: Day03(),
    4: Day04(),
    5: Day05(),
    6: Day06(),
    7: Day07(),
    8: Day08(),
    9: Day09(),
    10: Day10(),
    12: Day11(),
    12: Day12(),
    13: Day13(),
    14: Day14(),
    15: Day15(),
    16: Day16(),
}


def main():
    argc = len(sys.argv)
    if argc < 2 or argc > 3:
        raise ValueError("Usage: aoc2021 <day> [test]")
    day = int(sys.argv[1])
    if day not in DAYS:
        raise ValueError(f"Unknown day : {sys.argv[1]}")
    test = (argc > 2 and sys.argv[2].lower() == "test")
    DAYS[day](test=test)


if __name__ == '__main__':
    main()
