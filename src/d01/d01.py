"""Day 1"""

from collections import Counter
from os.path import join
from base.day import Day, SolveInfo


# pylint: disable=R0903
class Day01(Day):
    """Historian Hysteria"""

    def solve(self) -> SolveInfo:
        left: list[int] = []
        right: list[int] = []

        with open(join("src", "d01", "input.txt"), encoding="utf-8") as f:
            line = f.readline()
            while line:
                left_val, right_val = line.split("   ")

                left.append(int(left_val))
                right.append(int(right_val))

                line = f.readline()

        left.sort()
        right.sort()

        pt_1_res = 0
        # pylint: disable=C0200
        for i in range(len(left)):
            pt_1_res += abs(left[i] - right[i])

        right_counts = Counter(right)

        pt_2_res = 0
        for val in left:
            if val in right_counts:
                pt_2_res += val * right_counts[val]

        return SolveInfo(str(pt_1_res), str(pt_2_res))
