"""Day 18"""

from collections import deque
from concurrent.futures import ProcessPoolExecutor
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path

# Named tuples not used to improve runtime performance


class Day18(Day):
    """RAM Run"""

    # pylint: disable=R0914
    def get_pt_1(
        self, rows: int, cols: int, byte_count: int, bytes_l: list[tuple[int, int]]
    ) -> int:
        grid: list[list[str]] = [["."] * cols for _ in range(rows)]

        for i in range(byte_count):
            row, col = bytes_l[i]
            grid[row][col] = "#"

        q: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
        seen: set[tuple[int, int]] = set()

        while len(q) > 0:
            grid_row, grid_col, dis = q.popleft()

            if grid_row < 0 or grid_row >= rows or grid_col < 0 or grid_col >= cols:
                continue

            if grid[grid_row][grid_col] == "#":
                continue

            seen_tpl = (grid_row, grid_col)
            if seen_tpl in seen:
                continue
            seen.add(seen_tpl)

            if grid_row == rows - 1 and grid_col == cols - 1:
                return dis

            for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                q.append((grid_row + row_diff, grid_col + col_diff, dis + 1))

        return -1

    # pylint: disable=R0914
    def get_pt_2(self, rows: int, cols: int, bytes_l: list[tuple[int, int]]) -> str:
        grid: list[list[str]] = [["."] * cols for _ in range(rows)]

        for row, col in bytes_l:
            grid[row][col] = "#"

            q: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
            seen: set[tuple[int, int]] = set()

            trapped = True
            while len(q) > 0:
                grid_row, grid_col, dis = q.popleft()

                if grid_row < 0 or grid_row >= rows or grid_col < 0 or grid_col >= cols:
                    continue

                if grid[grid_row][grid_col] == "#":
                    continue

                seen_tpl = (grid_row, grid_col)
                if seen_tpl in seen:
                    continue
                seen.add(seen_tpl)

                if grid_row == rows - 1 and grid_col == cols - 1:
                    trapped = False
                    break

                for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    q.append((grid_row + row_diff, grid_col + col_diff, dis + 1))

            if trapped:
                r = f"{row},{col}"
                return r

        return ""

    def solve(self) -> SolveInfo:
        with open(get_path("18"), encoding="utf-8") as f:
            line = f.readline()

            bytes_l: list[tuple[int, int]] = []

            while line:
                row = line[:-1] if line[-1] == "\n" else line[:]

                s = row.split(",")
                bytes_l.append((int(s[0]), int(s[1])))

                line = f.readline()

        with ProcessPoolExecutor() as executor:
            future1 = executor.submit(self.get_pt_1, 71, 71, 1024, bytes_l)
            future2 = executor.submit(self.get_pt_2, 71, 71, bytes_l)

            pt_1_res = future1.result()
            pt_2_res = future2.result()

            return SolveInfo(str(pt_1_res), pt_2_res)
