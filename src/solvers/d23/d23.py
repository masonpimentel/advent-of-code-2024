"""Day 23"""

from collections import defaultdict
from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=C0115
class Edge(NamedTuple):
    computer_1: str
    computer_2: str


class Day23(Day):
    """LAN Party"""

    def __init__(self) -> None:
        self.adj: dict[str, list[str]] = defaultdict(list)
        self.edges: set[Edge] = set()

    def find_third(self, first: str, second: str, thirds: list[str]) -> list[str]:
        res: list[str] = []

        for third in thirds:
            third_adj = self.adj[third]

            if first in third_adj and second in third_adj:
                res.append(third)

        return res

    def get_pt_1(self) -> str:
        tuples: list[list[str]] = []
        seen: set[str] = set()

        for first in self.adj:
            first_adj = self.adj[first]
            for i, second in enumerate(first_adj):
                for third in self.find_third(
                    first, second, first_adj[:i] + first_adj[i + 1 :]
                ):
                    tpl_l = [first, second, third]
                    tpl_l.sort()
                    tpl_s = str(tpl_l)
                    if tpl_s not in seen:
                        seen.add(tpl_s)
                        tuples.append(tpl_l)

        res = 0
        for tpl in tuples:
            for comp in tpl:
                if comp[0] == "t":
                    res += 1
                    break

        return str(res)

    def get_pt_2(self) -> str:
        best: list[str] = []
        all_computers = set(self.adj.keys())

        for first in self.adj:
            network = set([first])

            for new_computer in all_computers:
                is_all_connected = True

                for current_computer in network:
                    if Edge(new_computer, current_computer) not in self.edges:
                        is_all_connected = False
                        break

                if is_all_connected:
                    network.add(new_computer)

            if len(network) > len(best):
                best = list(network)

        return ",".join(sorted(best))

    def solve(self) -> SolveInfo:
        with open(get_path("23"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                entry = line[:-1] if line[-1] == "\n" else line[:]

                s = entry.split("-")
                l, r = s[0], s[1]

                self.adj[l].append(r)
                self.adj[r].append(l)

                self.edges.add(Edge(l, r))
                self.edges.add(Edge(r, l))

                line = f.readline()

        return SolveInfo(self.get_pt_1(), self.get_pt_2())
