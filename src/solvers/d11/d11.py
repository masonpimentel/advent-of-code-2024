"""Day 11"""

from collections import defaultdict
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=R0903
class Day11(Day):
    """Plutonian Pebbles"""

    PT_1_BLINKS = 25
    PT_2_BLINKS = 75

    # pylint: disable=R0914
    def solve(self) -> SolveInfo:
        pt_1_res = ""
        pt_2_res = ""

        vals: dict[str, int] = defaultdict(int)
        with open(get_path("11"), encoding="utf-8") as f:
            line = f.readline()

            for v in line.split(" "):
                vals[v] += 1

        for i in range(self.PT_2_BLINKS):
            new_vals: dict[str, int] = defaultdict(int)

            for k, val in vals.items():
                if k == "0":
                    new_vals["1"] += val
                elif len(k) % 2 == 0:
                    l = len(k)
                    split = l // 2

                    left = int(k[:split])
                    right = int(k[split:])

                    new_vals[str(left)] += val
                    new_vals[str(right)] += val
                else:
                    new_int = int(k) * 2024
                    new_vals[str(new_int)] += val

            vals = new_vals

            if i == self.PT_1_BLINKS - 1:
                pt_1_res = str(sum(vals.values()))

        pt_2_res = str(sum(vals.values()))

        return SolveInfo(pt_1_res, pt_2_res)
