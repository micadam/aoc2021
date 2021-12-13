import copy
from collections import defaultdict, Counter
from queue import Queue
from typing import Dict, List, Set, TextIO

from ..day import Day

START = "start"
END = "end"
SEP = "-"


class Path:
    def __init__(self, start):
        self.segments: List[str] = [start]
        self.double_visit = False

    def visit(self, node):
        if node.islower() and node in self.segments:
            self.double_visit = True
        self.segments.append(node)
        return self

    def last(self):
        return self.segments[-1]

    def copy(self):
        return copy.deepcopy(self)

    @property
    def has_double_visit(self):
        return self.double_visit

    def __contains__(self, node):
        return node in self.segments

    def __repr__(self):
        return ",".join(self.segments)

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other):
        if not isinstance(other, Path):
            return False
        return self.segments == other.segments


class Day12(Day):
    def __init__(self):
        super().__init__("12", same_inputs_all=True)

    def __count_paths(self, f: TextIO, double_allowed: bool):
        edges: Dict[str, Set[str]] = defaultdict(set)
        all_paths = set()
        for line in f:
            line = line.strip()
            x, y = line.split(SEP)
            if y != START and x != END:
                edges[x].add(y)
            if x != START and y != END:
                edges[y].add(x)
        paths = Queue()
        paths.put(Path(START))
        while paths.qsize():
            path = paths.get()
            for new in edges[path.last()]:
                if new == END:
                    all_paths.add(path.copy().visit(new))
                    continue
                elif new.islower() and new in path and \
                        (not double_allowed or path.has_double_visit):
                    continue
                paths.put(path.copy().visit(new))
        return len(all_paths)

    def part1(self, f: TextIO):
        return self.__count_paths(f, False)

    def part2(self, f: TextIO):
        return self.__count_paths(f, True)
