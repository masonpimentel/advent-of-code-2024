"""Day 2"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class Day02(Day):
    """Red-Nosed Reports"""

    def check_level(self, vals: list[int]) -> bool:
        is_increase = vals[1] > vals[0]

        for i in range(len(vals) - 1):
            diff = abs(vals[i + 1] - vals[i])
            if diff < 1 or diff > 3:
                return False

            if (is_increase and vals[i + 1] <= vals[i]) or (
                not is_increase and vals[i + 1] >= vals[i]
            ):
                return False

        return True

    def solve(self) -> SolveInfo:
        levels: list[list[int]] = []

        with open(get_path("02"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                levels.append([int(v) for v in line.split(" ")])
                line = f.readline()

        pt_1_res = 0
        pt_2_res = 0
        for level in levels:
            orig_result = self.check_level(level)

            if orig_result:
                pt_1_res += 1
                pt_2_res += 1
            else:
                for i in range(len(level)):
                    line_with_i_removed = self.check_level(level[:i] + level[i + 1 :])
                    if line_with_i_removed:
                        pt_2_res += 1
                        break

        return SolveInfo(str(pt_1_res), str(pt_2_res))
