"""Day 8"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path, get_grid


class Day08(Day):
    """Resonant Collinearity"""

    def __init__(self) -> None:
        self.grid: list[list[str]] = []
        self.rows = -1
        self.cols = -1

    def scan(
        self, row: int, col: int, res_pt_1: list[list[int]], res_pt_2: list[list[int]]
    ) -> None:
        for scan_row in range(self.rows):
            for scan_col in range(self.cols):
                if scan_row == row and scan_col == col:
                    continue

                if self.grid[scan_row][scan_col] == self.grid[row][col]:
                    row_diff = scan_row - row
                    col_diff = scan_col - col

                    anti_row_pt_1 = scan_row + row_diff
                    anti_col_pt_1 = scan_col + col_diff

                    if (
                        self.rows > anti_row_pt_1 >= 0
                        and self.cols > anti_col_pt_1 >= 0
                    ):
                        res_pt_1[anti_row_pt_1][anti_col_pt_1] = (
                            res_pt_1[anti_row_pt_1][anti_col_pt_1] or True
                        )

                    anti_row_pt2 = row
                    anti_col_pt2 = col

                    while (
                        self.rows > anti_row_pt2 >= 0 and self.cols > anti_col_pt2 >= 0
                    ):
                        res_pt_2[anti_row_pt2][anti_col_pt2] = (
                            res_pt_2[anti_row_pt2][anti_col_pt2] or True
                        )

                        anti_row_pt2 += row_diff
                        anti_col_pt2 += col_diff

    def solve(self) -> SolveInfo:
        with open(get_path("08"), encoding="utf-8") as f:
            self.grid, self.rows, self.cols = get_grid(f)

        res_pt_1: list[list[int]] = [[False] * self.cols for _ in range(self.rows)]
        res_pt_2: list[list[int]] = [[False] * self.cols for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != ".":
                    self.scan(row, col, res_pt_1, res_pt_2)

        pt_1_res = 0
        for res_row in res_pt_1:
            for v in res_row:
                pt_1_res += 1 if v else 0
        pt_2_res = 0
        for res_row in res_pt_2:
            for v in res_row:
                pt_2_res += 1 if v else 0

        return SolveInfo(str(pt_1_res), str(pt_2_res))
