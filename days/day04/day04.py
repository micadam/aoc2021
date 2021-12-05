from typing import TextIO

from ..day import Day


class BoardLine:
    def __init__(self, numbers):
        self.numbers = set(numbers)

    def remove(self, number):
        self.numbers.discard(number)
        return len(self.numbers) == 0


class Board:
    def __init__(self, numbers):
        self.numbers = set(n for num in numbers for n in num)
        self.lines = [BoardLine(num) for num in numbers]
        self.lines.extend([BoardLine([num[i] for num in numbers])
                           for i in range(len(numbers[0]))])

    def call(self, number):
        self.numbers.discard(number)
        for line in self.lines:
            if line.remove(number):
                return sum(self.numbers) * number


class Day04(Day):
    def __init__(self):
        super().__init__("04", same_inputs_all=True)

    def __get_boards(self, f: TextIO):
        calls = list(map(int, f.readline().split(",")))
        # Skip empty line
        f.readline()
        board = []
        boards = []
        for line in f:
            if line == "\n":
                boards.append(Board(board))
                board = []
                continue
            numbers = list(map(int, line.split()))
            board.append(numbers)
        # Last board might not have had a newlne after it
        if len(board) > 0:
            boards.append(Board(board))
        return set(boards), calls

    def part1(self, f: TextIO):
        boards, calls = self.__get_boards(f)
        for call in calls:
            for board in boards:
                if (ret := board.call(call)) is not None:
                    return ret

    def part2(self, f: TextIO):
        boards, calls = self.__get_boards(f)
        for call in calls:
            new_boards = []
            for board in boards:
                if (ret := board.call(call)) is not None:
                    if len(boards) == 1:
                        return ret
                else:
                    new_boards.append(board)
            boards = set(new_boards)
