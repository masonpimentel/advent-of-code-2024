"""Day 12"""

from collections import deque
from typing import NamedTuple
from enum import Enum
from solvers.base.day import Day
from solvers.base.types import SolveInfo, RowCol
from solvers.utils.helpers import get_path, get_grid, check_row_and_col


class DIRECTION(Enum):
    """4 possible directions"""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Pt2Seen(NamedTuple):
    """Info to cache for part 2"""

    row: int
    col: int
    direction: DIRECTION


class Day12(Day):
    """Garden Groups"""

    TOMBSTONE = "."

    def __init__(self) -> None:
        self.pt_1_grid: list[list[str]] = []
        self.pt_2_grid: list[list[str]] = []
        self.orig_grid: list[list[str]] = []
        self.rows = -1
        self.cols = -1

    def explore_pt_1(self, row: int, col: int, plant: str) -> int:
        q: deque[RowCol] = deque([RowCol(row, col)])

        area = 0
        perim = 0

        while len(q) > 0:
            check_row, check_col = q.popleft()

            if self.pt_1_grid[check_row][check_col] != plant:
                continue

            self.pt_1_grid[check_row][check_col] = self.TOMBSTONE
            area += 1

            perim += 4
            for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                add_row = check_row + row_diff
                add_col = check_col + col_diff

                if self.rows > add_row >= 0 and self.cols > add_col >= 0:
                    if self.orig_grid[add_row][add_col] == plant:
                        perim -= 1

                    q.append(RowCol(add_row, add_col))

        return area * perim

    def explore_pt_2(self, row: int, col: int, plant: str) -> int:
        q: deque[RowCol] = deque([RowCol(row, col)])

        area = 0
        sides = 0

        seen: set[Pt2Seen] = set()

        def mark_horizontal(
            boundary: int, check: bool, direc: DIRECTION, check_row: int, check_col: int
        ) -> int:
            if (check or self.orig_grid[boundary][check_col] != plant) and (
                check_row,
                check_col,
                direc,
            ) not in seen:
                for seen_col in range(check_col - 1, -1, -1):
                    if self.orig_grid[check_row][seen_col] == plant and (
                        check or self.orig_grid[boundary][seen_col] != plant
                    ):
                        seen.add(Pt2Seen(check_row, seen_col, direc))
                    else:
                        break
                for seen_col in range(check_col + 1, self.cols):
                    if self.orig_grid[check_row][seen_col] == plant and (
                        check or self.orig_grid[boundary][seen_col] != plant
                    ):
                        seen.add(Pt2Seen(check_row, seen_col, direc))
                    else:
                        break
                return 1

            return 0

        def mark_vertical(
            boundary: int, check: bool, direc: DIRECTION, check_row: int, check_col: int
        ) -> int:
            if (check or self.orig_grid[check_row][boundary] != plant) and (
                check_row,
                check_col,
                direc,
            ) not in seen:
                for seen_row in range(check_row - 1, -1, -1):
                    if self.orig_grid[seen_row][check_col] == plant and (
                        check or self.orig_grid[seen_row][boundary] != plant
                    ):
                        seen.add(Pt2Seen(seen_row, check_col, direc))
                    else:
                        break
                for seen_row in range(check_row + 1, self.rows):
                    if self.orig_grid[seen_row][check_col] == plant and (
                        check or self.orig_grid[seen_row][boundary] != plant
                    ):
                        seen.add(Pt2Seen(seen_row, check_col, direc))
                    else:
                        break
                return 1

            return 0

        while len(q) > 0:
            check_row, check_col = q.popleft()

            if check_row_and_col(check_row, check_col, self.rows, self.cols):
                continue

            if self.pt_2_grid[check_row][check_col] != plant:
                continue

            self.pt_2_grid[check_row][check_col] = self.TOMBSTONE
            area += 1

            for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                q.append(RowCol(check_row + row_diff, check_col + col_diff))

            boundary = check_row - 1
            sides += mark_horizontal(
                boundary, boundary < 0, DIRECTION.UP, check_row, check_col
            )

            boundary = check_row + 1
            sides += mark_horizontal(
                boundary, boundary >= self.rows, DIRECTION.DOWN, check_row, check_col
            )

            boundary = check_col + 1
            sides += mark_vertical(
                boundary, boundary >= self.cols, DIRECTION.RIGHT, check_row, check_col
            )

            boundary = check_col - 1
            sides += mark_vertical(
                boundary, boundary < 0, DIRECTION.LEFT, check_row, check_col
            )

        return area * sides

    def solve(self) -> SolveInfo:
        with open(get_path("12"), encoding="utf-8") as f:
            self.orig_grid, self.rows, self.cols = get_grid(f)

        self.pt_1_grid = [list(row) for row in self.orig_grid]
        self.pt_2_grid = [list(row) for row in self.orig_grid]

        pt_1_res = 0
        pt_2_res = 0
        for row in range(self.rows):
            for col in range(self.cols):
                v = self.orig_grid[row][col]

                if v != self.TOMBSTONE:
                    res = self.explore_pt_1(row, col, v)
                    pt_1_res += res

                    res = self.explore_pt_2(row, col, v)
                    pt_2_res += res

        return SolveInfo(str(pt_1_res), str(pt_2_res))
