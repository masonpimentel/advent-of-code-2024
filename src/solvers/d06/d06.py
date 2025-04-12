"""Day 6"""

from concurrent.futures import ProcessPoolExecutor
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_grid, get_path

# Named tuples not used to improve runtime performance


class Day06(Day):
    """Guard Gallivant"""

    PARALLEL_CHUNK_SIZE = 50

    def __init__(self) -> None:
        self.grid: list[list[str]] = []
        self.pt_1_positions: list[list[str]] = []
        self.rows = -1
        self.cols = -1
        self.start_row = -1
        self.start_col = -1

    def make_move(
        self, row_pos: int, col_pos: int, direc: str
    ) -> tuple[bool, int, int, str]:
        breakout = (True, -1, -1, "")
        new_row = row_pos
        new_col = col_pos
        new_direc = direc

        match direc:
            case "up":
                if row_pos == 0:
                    return breakout

                if self.grid[row_pos - 1][col_pos] == "#":
                    new_direc = "right"
                else:
                    new_row -= 1
            case "right":
                if col_pos == self.cols - 1:
                    return breakout

                if self.grid[row_pos][col_pos + 1] == "#":
                    new_direc = "down"
                else:
                    new_col += 1
            case "down":
                if row_pos == self.rows - 1:
                    return breakout

                if self.grid[row_pos + 1][col_pos] == "#":
                    new_direc = "left"
                else:
                    new_row += 1
            case "left":
                if col_pos == 0:
                    return breakout

                if self.grid[row_pos][col_pos - 1] == "#":
                    new_direc = "up"
                else:
                    new_col -= 1

        return (False, new_row, new_col, new_direc)

    def run_simulation(
        self, row_pos: int, col_pos: int, direc: str, set_positions: bool
    ) -> bool:
        seen: dict[int, dict[int, set[str]]] = {}

        while True:
            if (
                row_pos in seen
                and col_pos in seen[row_pos]
                and direc in seen[row_pos][col_pos]
            ):
                return True

            if set_positions:
                self.pt_1_positions[row_pos][col_pos] = "V"

            is_breakout, new_row, new_col, new_direc = self.make_move(
                row_pos, col_pos, direc
            )

            if is_breakout:
                break

            if row_pos not in seen:
                seen[row_pos] = {}
            if col_pos not in seen[row_pos]:
                seen[row_pos][col_pos] = set()
            seen[row_pos][col_pos].add(direc)

            row_pos = new_row
            col_pos = new_col
            direc = new_direc

        return False

    def process_cell(self, args: tuple[int, int, str]) -> int:
        row, col, direc = args
        if self.grid[row][col] == "." and (
            row != self.start_row or col != self.start_col
        ):
            self.grid[row][col] = "#"
            res = self.run_simulation(self.start_row, self.start_col, direc, False)
            self.grid[row][col] = "."
            return 1 if res else 0
        return 0

    def solve(self) -> SolveInfo:
        with open(get_path("06"), encoding="utf-8") as f:
            self.grid, self.rows, self.cols = get_grid(f)

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == "^":
                    self.start_row = row
                    self.start_col = col

        direc = "up"

        self.pt_1_positions = [["."] * self.cols for _ in range(self.rows)]
        self.run_simulation(self.start_row, self.start_col, direc, True)
        pt_1_res = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.pt_1_positions[row][col] == "V":
                    pt_1_res += 1

        with ProcessPoolExecutor() as executor:
            tasks = [
                (row, col, direc)
                for row in range(self.rows)
                for col in range(self.cols)
            ]
            results = executor.map(
                self.process_cell, tasks, chunksize=self.PARALLEL_CHUNK_SIZE
            )

        pt_2_res = sum(results)

        return SolveInfo(str(pt_1_res), str(pt_2_res))
