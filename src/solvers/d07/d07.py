"""Day 7"""

from concurrent.futures import ProcessPoolExecutor
from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=C0115
class RecurseArgs(NamedTuple):
    tot: int
    cur: int
    vals: list[int]
    combine: bool


class Calibration(NamedTuple):
    result: int
    operators: list[int]


class Day07(Day):
    """Bridge Repair"""

    def rec(self, args: RecurseArgs) -> bool:
        tot, cur, vals, combine = args

        if len(vals) == 0:
            return tot == cur

        # add
        if self.rec(RecurseArgs(tot, cur + vals[0], vals[1:], combine)):
            return True
        # mul
        if self.rec(RecurseArgs(tot, cur * vals[0], vals[1:], combine)):
            return True
        # combine
        if combine and self.rec(
            RecurseArgs(tot, int(str(cur) + str(vals[0])), vals[1:], combine)
        ):
            return True

        return False

    def solve(self) -> SolveInfo:
        calibrations: list[Calibration] = []

        with open(get_path("07"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                tot, vals = line.split(": ")
                calibrations.append(
                    Calibration(int(tot), [int(x) for x in vals.split(" ")])
                )

                line = f.readline()

        pt_1_res = 0
        pt_2_res = 0

        with ProcessPoolExecutor() as executor:
            tasks = [
                RecurseArgs(calib_tot, calib_vals[0], calib_vals[1:], is_pt_2)
                for calib_tot, calib_vals in calibrations
                for is_pt_2 in [True, False]
            ]
            results = executor.map(self.rec, tasks)

        for (calib_tot, _, __, is_pt_2), r in zip(tasks, results):
            if r:
                if is_pt_2:
                    pt_2_res += calib_tot
                else:
                    pt_1_res += calib_tot

        return SolveInfo(str(pt_1_res), str(pt_2_res))
