"""Day 4"""

from enum import Enum
from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo, RowCol
from solvers.utils.helpers import get_grid, get_path


class Pattern(NamedTuple):
    """Cross pattern"""

    top_left: str
    top_right: str
    bottom_left: str
    bottom_right: str


class DIRECTION(Enum):
    """8 possible directions"""

    UP = 0
    UP_RIGHT = 1
    RIGHT = 2
    DOWN_RIGHT = 3
    DOWN = 4
    DOWN_LEFT = 5
    LEFT = 6
    UP_LEFT = 7


class Day04(Day):
    """Ceres Search"""

    def __init__(self) -> None:
        self.mat: list[list[str]] = []
        self.rows = 0
        self.cols = 0

    def new_row_and_col(self, row: int, col: int, d: DIRECTION) -> RowCol:
        new_row = row
        new_col = col
        match d:
            case DIRECTION.UP:
                new_row = row - 1
            case DIRECTION.UP_RIGHT:
                new_row = row - 1
                new_col = col + 1
            case DIRECTION.RIGHT:
                new_col = col + 1
            case DIRECTION.DOWN_RIGHT:
                new_row = row + 1
                new_col = col + 1
            case DIRECTION.DOWN:
                new_row = row + 1
            case DIRECTION.DOWN_LEFT:
                new_row = row + 1
                new_col = col - 1
            case DIRECTION.LEFT:
                new_col = col - 1
            case DIRECTION.UP_LEFT:
                new_row = row - 1
                new_col = col - 1

        return RowCol(new_row, new_col)

    def search(self, row: int, col: int, looking_for: str, d: DIRECTION) -> bool:
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False

        if self.mat[row][col] != looking_for:
            return False

        new_row, new_col = self.new_row_and_col(row, col, d)

        if looking_for == "M":
            return self.search(new_row, new_col, "A", d)
        if looking_for == "A":
            return self.search(new_row, new_col, "S", d)

        return True

    def count_words(self, row: int, col: int) -> int:
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return 0

        if self.mat[row][col] != "X":
            return 0

        res = 0
        for d in DIRECTION:
            new_row, new_col = self.new_row_and_col(row, col, d)

            if self.search(new_row, new_col, "M", d):
                res += 1

        return res

    def check_pattern(self, row: int, col: int, pattern: Pattern) -> bool:
        return (
            self.mat[row][col] == pattern.top_left
            and self.mat[row][col + 2] == pattern.top_right
            and self.mat[row + 2][col] == pattern.bottom_left
            and self.mat[row + 2][col + 2] == pattern.bottom_right
        )

    def get_pt_1(self) -> str:
        res = 0
        for row in range(self.rows):
            for col in range(self.cols):
                res += self.count_words(row, col)

        return str(res)

    def get_pt_2(self) -> str:
        patterns: list[Pattern] = [
            Pattern("M", "S", "M", "S"),
            Pattern("M", "M", "S", "S"),
            Pattern("S", "M", "S", "M"),
            Pattern("S", "S", "M", "M"),
        ]

        res = 0
        for row in range(self.rows - 2):
            for col in range(self.cols - 2):
                if self.mat[row + 1][col + 1] == "A":
                    if any(self.check_pattern(row, col, p) for p in patterns):
                        res += 1

        return str(res)

    def solve(self) -> SolveInfo:
        with open(get_path("04"), encoding="utf-8") as f:
            self.mat, self.rows, self.cols = get_grid(f)

        return SolveInfo(self.get_pt_1(), self.get_pt_2())
