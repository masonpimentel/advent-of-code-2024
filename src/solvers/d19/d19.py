"""Day 19"""

from os.path import join
from base.day import Day, SolveInfo


class Day19(Day):
    """Linen Layout"""

    def __init__(self) -> None:
        self.possible: set[str] = set()
        self.dp: dict[str, int] = {}

    def rec(self, pat: str) -> int:
        if pat == "":
            return 1

        res = 0
        for i in range(len(pat)):
            complete = pat[: i + 1]

            if complete in self.possible:
                new_pat = pat[i + 1 :]

                if new_pat in self.dp:
                    attempt = self.dp[new_pat]
                else:
                    attempt = self.rec(new_pat)
                    self.dp[new_pat] = attempt

                res += attempt

        return res

    def solve(self) -> SolveInfo:
        designs: list[str] = []

        with open(join("src", "d19", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            self.possible = set(line[:-1].split(", "))

            line = f.readline()
            line = f.readline()

            while line:
                designs.append(line[:-1] if line[-1] == "\n" else line)
                line = f.readline()

        pt_1_res = 0
        pt_2_res = 0

        for design in designs:
            attempt = self.rec(design)

            pt_1_res += 1 if attempt > 0 else 0
            pt_2_res += attempt

        return SolveInfo(str(pt_1_res), str(pt_2_res))
