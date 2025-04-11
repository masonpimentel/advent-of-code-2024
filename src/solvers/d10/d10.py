"""Day 10"""

from os.path import join
from solvers.interfaces.day import Day, SolveInfo
from solvers.utils.helpers import get_path, get_grid


class Day10(Day):
    """Hoof It"""

    def __init__(self) -> None:
        self.rows = -1
        self.cols = -1
        self.int_grid: list[list[int]] = []

    def dfs(self, args: tuple[int, int, int, set[str], set[str]]) -> None:
        row, col, height, seen, peaks = args

        s = str((row, col))
        if s in seen:
            return

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return

        if self.int_grid[row][col] != height:
            return

        if self.int_grid[row][col] == 9:
            peaks.add(s)
            return

        for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            seen.add(s)
            self.dfs((row + row_diff, col + col_diff, height + 1, seen, peaks))
            seen.remove(s)

        return

    def dfs_pt_2(self, row: int, col: int, height: int, seen: set[str]) -> int:
        s = str((row, col))
        if s in seen:
            return 0

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return 0

        if self.int_grid[row][col] != height:
            return 0

        if self.int_grid[row][col] == 9:
            return 1

        res = 0
        for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            seen.add(s)
            res += self.dfs_pt_2(row + row_diff, col + col_diff, height + 1, seen)
            seen.remove(s)

        return res

    def solve(self) -> tuple[str, str]:
        with open(get_path("10"), encoding="utf-8") as f:
            grid, self.rows, self.cols = get_grid(f)

        self.int_grid = [[int(value) for value in row] for row in grid]

        pt_1_res = 0
        pt_2_res = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if self.int_grid[row][col] == 0:

                    peaks: set[str] = set()
                    self.dfs((row, col, 0, set(), peaks))
                    trails = len(peaks)

                    pt_1_res += trails
                    pt_2_res += self.dfs_pt_2(row, col, 0, set())

        return (str(pt_1_res), str(pt_2_res))
