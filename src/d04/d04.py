"""Day 4"""

from os.path import join
from enum import Enum
from base.day import Day
from helpers import get_grid


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

    def new_row_and_col(self, row: int, col: int, d: DIRECTION) -> tuple[int, int]:
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

        return (new_row, new_col)

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

    def check_pattern(
        self, row: int, col: int, pattern: tuple[str, str, str, str]
    ) -> bool:
        return (
            self.mat[row][col] == pattern[0]
            and self.mat[row][col + 2] == pattern[1]
            and self.mat[row + 2][col] == pattern[2]
            and self.mat[row + 2][col + 2] == pattern[3]
        )

    def part_one(self) -> str:
        res = 0
        for row in range(self.rows):
            for col in range(self.cols):
                res += self.count_words(row, col)

        return str(res)

    def part_two(self) -> str:
        patterns = [
            # M S
            #  A
            # M S
            ("M", "S", "M", "S"),
            # M M
            #  A
            # S S
            ("M", "M", "S", "S"),
            # S M
            #  A
            # S M
            ("S", "M", "S", "M"),
            # S S
            #  A
            # M M
            ("S", "S", "M", "M"),
        ]

        res = 0
        for row in range(self.rows - 2):
            for col in range(self.cols - 2):
                if self.mat[row + 1][col + 1] == "A":
                    if any(self.check_pattern(row, col, p) for p in patterns):
                        res += 1

        return str(res)

    def solve(self) -> tuple[str, str]:
        with open(join("src", "d04", "input.txt"), encoding="utf-8") as f:
            self.mat, self.rows, self.cols = get_grid(f)

        pt_1_res = self.part_one()
        pt_2_res = self.part_two()

        return (pt_1_res, pt_2_res)
