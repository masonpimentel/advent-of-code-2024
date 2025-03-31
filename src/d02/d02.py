"""Day 2"""

from os.path import join
from base.day import Day, SolveInfo


class Day02(Day):
    """Red-Nosed Reports"""

    def check_level(self, vals: list[int]) -> bool:
        is_safe = True

        is_increase = vals[1] > vals[0]
        for i in range(len(vals) - 1):
            diff = abs(vals[i + 1] - vals[i])
            if diff < 1 or diff > 3:
                is_safe = False
                break

            if is_increase and vals[i + 1] <= vals[i]:
                is_safe = False
                break
            if not is_increase and vals[i + 1] >= vals[i]:
                is_safe = False
                break

        return is_safe

    def solve(self) -> SolveInfo:
        levels: list[list[int]] = []

        with open(join("src", "d02", "input.txt"), encoding="utf-8") as f:
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
