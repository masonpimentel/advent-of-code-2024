"""Day 20"""

from sys import setrecursionlimit, maxsize
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path, get_grid, check_row_and_col

# Named tuples not used to improve runtime performance


class Day20(Day):
    """Race Condition"""

    PT_1_JUMP = 2
    PT_2_JUMP = 20
    THRESHOLD = 100

    def __init__(self) -> None:
        self.grid: list[list[str]] = []
        self.rows = -1
        self.cols = -1
        self.dp: list[list[int]] = []
        self.seen: list[list[bool]] = []

    def move(self, row: int, col: int, seen: list[list[bool]]) -> int:
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return maxsize

        if self.grid[row][col] == "#":
            return maxsize

        if seen[row][col]:
            return maxsize

        if self.grid[row][col] == "E":
            self.dp[row][col] = 0
            return 0

        if self.dp[row][col] != -1:
            return self.dp[row][col]

        res = maxsize

        seen[row][col] = True
        for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            check_row = row + row_diff
            check_col = col + col_diff

            rec_res = self.move(check_row, check_col, seen)

            res = min(res, 1 + rec_res)

        seen[row][col] = False
        self.dp[row][col] = res

        return res

    def get_pt_1_slots(self) -> set[tuple[int, int]]:
        res: set[tuple[int, int]] = set()

        for row in range(-self.PT_1_JUMP, self.PT_1_JUMP + 1):
            for col in range(-self.PT_1_JUMP, self.PT_1_JUMP + 1):
                dist = abs(row) + abs(col)

                if dist == self.PT_1_JUMP:
                    res.add((row, col))

        return res

    def get_pt_2_slots(self) -> set[tuple[int, int, int]]:
        res: set[tuple[int, int, int]] = set()

        for row in range(-self.PT_2_JUMP, self.PT_2_JUMP + 1):
            for col in range(-self.PT_2_JUMP, self.PT_2_JUMP + 1):
                dist = abs(row) + abs(col)

                if dist <= self.PT_2_JUMP:
                    res.add((row, col, dist))

        return res

    def check_pt_1_slots(self, row: int, col: int) -> int:
        slots = self.get_pt_1_slots()

        res = 0
        for row_diff, col_diff in slots:
            check_row = row + row_diff
            check_col = col + col_diff

            # pylint: disable=R0801
            if check_row_and_col(check_row, check_col, self.rows, self.cols):
                continue

            if self.dp[check_row][check_col] == -1:
                continue

            cheat_adv = (
                self.dp[row][col] - self.dp[check_row][check_col] - self.PT_1_JUMP
            )

            if cheat_adv >= self.THRESHOLD:
                res += 1

        return res

    def check_pt_2_slots(self, row: int, col: int) -> int:
        slots = self.get_pt_2_slots()

        res = 0
        for row_diff, col_diff, jump in slots:
            check_row = row + row_diff
            check_col = col + col_diff

            if (
                check_row < 0
                or check_row >= self.rows
                or check_col < 0
                or check_col >= self.cols
            ):
                continue

            if self.dp[check_row][check_col] == -1:
                continue

            cheat_adv = self.dp[row][col] - self.dp[check_row][check_col] - jump

            if cheat_adv >= self.THRESHOLD:
                res += 1

        return res

    def solve(self) -> SolveInfo:
        setrecursionlimit(10**6)

        with open(get_path("20"), encoding="utf-8") as f:
            self.grid, self.rows, self.cols = get_grid(f)

        self.dp = [[-1] * self.cols for _ in range(self.rows)]
        self.seen = [[False] * self.cols for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == "S":
                    self.move(row, col, self.seen)

        pt_1_res = 0
        pt_2_res = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.dp[row][col] != -1:
                    pt_1_res += self.check_pt_1_slots(row, col)
                    pt_2_res += self.check_pt_2_slots(row, col)

        return SolveInfo(str(pt_1_res), str(pt_2_res))
