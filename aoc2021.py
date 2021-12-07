import sys
from days.day01 import Day01
from days.day02 import Day02
from days.day03 import Day03
from days.day04 import Day04
from days.day05 import Day05
from days.day06 import Day06

DAYS = {
    1: Day01(),
    2: Day02(),
    3: Day03(),
    4: Day04(),
    5: Day05(),
    6: Day06(),
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
