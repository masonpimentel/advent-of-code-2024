from collections import deque
from os.path import join
from base.day import Day

class Day18(Day):
    def solve(self):
        with open(join("src", "d18", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            bytes: list[tuple[int, int]] = []

            while line:
                row = line[:-1] if line[-1] == "\n" else line[:]

                s = row.split(",")
                bytes.append((int(s[0]), int(s[1])))

                line = f.readline()

            def part_1(rows: int, cols: int, byte_count: int) -> int:
                grid: list[list[str]] = [["."] * cols for _ in range(rows)]

                for i in range(byte_count):
                    row, col = bytes[i]

                    grid[row][col] = "#"

                q: list[tuple[int, int, int]] = deque([(0, 0, 0)])
                seen: set[str] = set()

                while len(q) > 0:
                    grid_row, grid_col, dis = q.popleft()

                    if (
                        grid_row < 0
                        or grid_row >= rows
                        or grid_col < 0
                        or grid_col >= cols
                    ):
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

            def part_2(rows: int, cols: int):
                grid: list[list[str]] = [["."] * cols for _ in range(rows)]

                l = len(bytes)
                for i in range(l):
                    row, col = bytes[i]

                    grid[row][col] = "#"

                    q: list[tuple[int, int, int]] = deque([(0, 0, 0)])
                    seen: set[str] = set()

                    trapped = True
                    while len(q) > 0:
                        grid_row, grid_col, dis = q.popleft()

                        if (
                            grid_row < 0
                            or grid_row >= rows
                            or grid_col < 0
                            or grid_col >= cols
                        ):
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
                            q.append(
                                (grid_row + row_diff, grid_col + col_diff, dis + 1)
                            )

                    if trapped:
                        r = f"{row},{col}"
                        return r

            pt_1_res = part_1(71, 71, 1024)
            pt_2_res = part_2(71, 71)

            return (str(pt_1_res), pt_2_res)
