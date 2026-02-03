"""Day 16"""

from heapq import heappop, heappush
from typing import NamedTuple
from enum import Enum
from collections import defaultdict
from solvers.base.day import Day
from solvers.base.types import SolveInfo, RowCol
from solvers.utils.helpers import get_path, get_grid


class DIRECTION(Enum):
    """4 possible directions"""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class NewPosition(NamedTuple):
    """Components of a new position"""

    point_cost: int
    row_diff: int
    col_diff: int
    new_direction: int


class Day16(Day):
    """Reindeer Maze"""

    NEW_POSITIONS: dict[int, list[NewPosition]] = {
        DIRECTION.NORTH.value: [
            NewPosition(1, -1, 0, DIRECTION.NORTH.value),
            NewPosition(1000, 0, 0, DIRECTION.EAST.value),
            NewPosition(2000, 0, 0, DIRECTION.SOUTH.value),
            NewPosition(1000, 0, 0, DIRECTION.WEST.value),
        ],
        DIRECTION.EAST.value: [
            NewPosition(1000, 0, 0, DIRECTION.NORTH.value),
            NewPosition(1, 0, 1, DIRECTION.EAST.value),
            NewPosition(1000, 0, 0, DIRECTION.SOUTH.value),
            NewPosition(2000, 0, 0, DIRECTION.WEST.value),
        ],
        DIRECTION.SOUTH.value: [
            NewPosition(2000, 0, 0, DIRECTION.NORTH.value),
            NewPosition(1000, 0, 0, DIRECTION.EAST.value),
            NewPosition(1, 1, 0, DIRECTION.SOUTH.value),
            NewPosition(1000, 0, 0, DIRECTION.WEST.value),
        ],
        DIRECTION.WEST.value: [
            NewPosition(1000, 0, 0, DIRECTION.NORTH.value),
            NewPosition(2000, 0, 0, DIRECTION.EAST.value),
            NewPosition(1000, 0, 0, DIRECTION.SOUTH.value),
            NewPosition(1, 0, -1, DIRECTION.WEST.value),
        ],
    }

    def __init__(self) -> None:
        self.grid: list[list[str]] = []
        self.rows = -1
        self.cols = -1

    def get_distance_from_start(
        self, start_tpl: RowCol
    ) -> list[list[defaultdict[int, int]]]:
        res: list[list[defaultdict[int, int]]] = [
            [defaultdict(lambda: -1) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

        h: list[NewPosition] = [
            NewPosition(0, start_tpl[0], start_tpl[1], DIRECTION.EAST.value)
        ]

        while len(h) > 0:
            dist, cur_row, cur_col, d = heappop(h)

            if (
                cur_row < 0
                or cur_row >= self.rows
                or cur_col < 0
                or cur_col >= self.cols
            ):
                continue

            if res[cur_row][cur_col][d] > -1 or self.grid[cur_row][cur_col] == "#":
                continue

            res[cur_row][cur_col][d] = dist

            for cost, row_diff, col_diff, new_dir in self.NEW_POSITIONS[d]:
                heappush(
                    h,
                    NewPosition(
                        dist + cost, cur_row + row_diff, cur_col + col_diff, new_dir
                    ),
                )

        return res

    def get_distance_from_end(
        self, end_tpl: RowCol
    ) -> list[list[defaultdict[int, int]]]:
        res: list[list[defaultdict[int, int]]] = [
            [defaultdict(lambda: -1) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

        h: list[NewPosition] = [
            NewPosition(0, end_tpl[0], end_tpl[1], start_d.value)
            for start_d in DIRECTION
        ]

        while len(h) > 0:
            dist, cur_row, cur_col, d = heappop(h)

            if (
                cur_row < 0
                or cur_row >= self.rows
                or cur_col < 0
                or cur_col >= self.cols
            ):
                continue

            if res[cur_row][cur_col][d] > -1 or self.grid[cur_row][cur_col] == "#":
                continue

            res[cur_row][cur_col][d] = dist

            for cost, row_diff, col_diff, new_dir in self.NEW_POSITIONS[d]:
                heappush(
                    h,
                    NewPosition(
                        dist + cost, cur_row + row_diff, cur_col + col_diff, new_dir
                    ),
                )

        return res

    def solve(self) -> SolveInfo:
        with open(get_path("16"), encoding="utf-8") as f:
            self.grid, self.rows, self.cols = get_grid(f)

        start_tpl = RowCol(-1, -1)
        end_tpl = RowCol(-1, -1)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == "S":
                    start_tpl = RowCol(row, col)
                elif self.grid[row][col] == "E":
                    end_tpl = RowCol(row, col)

        flip: dict[int, int] = {
            DIRECTION.NORTH.value: DIRECTION.SOUTH.value,
            DIRECTION.EAST.value: DIRECTION.WEST.value,
            DIRECTION.SOUTH.value: DIRECTION.NORTH.value,
            DIRECTION.WEST.value: DIRECTION.EAST.value,
        }

        from_start = self.get_distance_from_start(start_tpl)
        from_end = self.get_distance_from_end(end_tpl)

        path: list[list[int]] = [[0] * self.cols for _ in range(self.rows)]

        pt_1_res = min(from_start[end_tpl[0]][end_tpl[1]].values())
        for row in range(self.rows):
            for col in range(self.cols):
                for d in DIRECTION:
                    if (
                        from_end[row][col][d.value]
                        == pt_1_res - from_start[row][col][flip[d.value]]
                    ):
                        path[row][col] = 1
                        break

        pt_2_res = 0
        for path_row in path:
            pt_2_res += sum(path_row)

        return SolveInfo(str(pt_1_res), str(pt_2_res))
