"""Day 7"""

from os.path import join
from base.day import Day


class Day07(Day):
    """Bridge Repair"""

    def rec(self, tot: int, cur: int, vals: list[int], combine: bool) -> bool:
        if len(vals) == 0:
            return tot == cur

        # add
        if self.rec(tot, cur + vals[0], vals[1:], combine):
            return True
        # mul
        if self.rec(tot, cur * vals[0], vals[1:], combine):
            return True
        # combine
        if combine and self.rec(tot, int(str(cur) + str(vals[0])), vals[1:], combine):
            return True

        return False

    def solve(self) -> tuple[str, str]:
        calibrations: list[tuple[int, list[int]]] = []

        with open(join("src", "d07", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                tot, vals = line.split(": ")
                calibrations.append((int(tot), [int(x) for x in vals.split(" ")]))

                line = f.readline()

        pt_1_res = 0
        pt_2_res = 0
        for calib_tot, calib_vals in calibrations:
            if self.rec(calib_tot, calib_vals[0], calib_vals[1:], False):
                pt_1_res += calib_tot

            if self.rec(calib_tot, calib_vals[0], calib_vals[1:], True):
                pt_2_res += calib_tot

        return (str(pt_1_res), str(pt_2_res))
