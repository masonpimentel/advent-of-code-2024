from os.path import join
from base.day import Day

class Day10(Day):
    def solve(self):
        with open(join("src", "d10", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            grid: list[list[int]] = []

            while line:
                row = [c for c in line]

                if row[-1] == "\n":
                    row = row[:-1]

                row = [int(c) if c != "." else -1 for c in row]

                grid.append(row)
                line = f.readline()

            rows = len(grid)
            cols = len(grid[0])

            def dfs(
                row: int, col: int, height: int, seen: set[str], peaks: set[str]
            ) -> int:
                s = str((row, col))
                if s in seen:
                    return 0

                if row < 0 or row >= rows or col < 0 or col >= cols:
                    return 0

                if grid[row][col] != height:
                    return 0

                if grid[row][col] == 9:
                    peaks.add(s)
                    return

                res = 0
                for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    seen.add(s)
                    dfs(row + row_diff, col + col_diff, height + 1, seen, peaks)
                    seen.remove(s)

                return res

            def dfs_pt_2(row: int, col: int, height: int, seen: set[str]) -> int:
                s = str((row, col))
                if s in seen:
                    return 0

                if row < 0 or row >= rows or col < 0 or col >= cols:
                    return 0

                if grid[row][col] != height:
                    return 0

                if grid[row][col] == 9:
                    return 1

                res = 0
                for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    seen.add(s)
                    res += dfs_pt_2(row + row_diff, col + col_diff, height + 1, seen)
                    seen.remove(s)

                return res

            pt_1_res = 0
            pt_2_res = 0

            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 0:
                        seen: set[str] = set()

                        peaks: set[str] = set()
                        dfs(row, col, 0, set(), peaks)
                        trails = len(peaks)

                        pt_1_res += trails
                        pt_2_res += dfs_pt_2(row, col, 0, set())


            return (str(pt_1_res), str(pt_2_res))
