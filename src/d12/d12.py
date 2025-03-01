from collections import deque

from os.path import join

TOMBSTONE = "."


class Day12:
    def solve(self):
        with open(join("src", "d12", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            untouched_grid: list[list[str]] = []
            grid: list[list[str]] = []
            grid_pt_2: list[list[str]] = []

            while line:
                row = [c for c in line]

                if row[-1] == "\n":
                    row = row[:-1]

                grid.append(row)
                grid_pt_2.append(row[:])
                untouched_grid.append(row[:])

                line = f.readline()

            rows = len(grid)
            cols = len(grid[0])

            def explore_region(
                row: int, col: int, type: str, rows: int, cols: int
            ) -> int:

                q: list[tuple[int, int]] = deque([(row, col)])

                area = 0
                perim = 0

                while len(q) > 0:
                    check_row, check_col = q.popleft()

                    if grid[check_row][check_col] != type:
                        continue

                    grid[check_row][check_col] = TOMBSTONE
                    area += 1

                    perim += 4
                    for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        add_row = check_row + row_diff
                        add_col = check_col + col_diff

                        if (
                            add_row >= 0
                            and add_row < rows
                            and add_col >= 0
                            and add_col < cols
                        ):
                            if untouched_grid[add_row][add_col] == type:
                                perim -= 1

                            q.append((add_row, add_col))

                return area * perim

            def explore_region_pt_2(
                row: int, col: int, type: str, rows: int, cols: int
            ) -> int:
                q: list[tuple[int, int]] = deque([(row, col)])

                area = 0
                sides = 0

                seen: set[tuple[int, str]] = set()

                while len(q) > 0:
                    check_row, check_col = q.popleft()

                    if (
                        check_row < 0
                        or check_row >= rows
                        or check_col < 0
                        or check_col >= cols
                    ):
                        continue

                    if grid_pt_2[check_row][check_col] != type:
                        continue

                    grid_pt_2[check_row][check_col] = TOMBSTONE
                    area += 1

                    for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        q.append((check_row + row_diff, check_col + col_diff))

                    # up
                    up_row = check_row - 1
                    no_up_row = up_row < 0
                    if (no_up_row or untouched_grid[up_row][check_col] != type) and (
                        check_row,
                        check_col,
                        "up",
                    ) not in seen:
                        for seen_col in range(check_col - 1, -1, -1):
                            if untouched_grid[check_row][seen_col] == type and (
                                no_up_row or untouched_grid[up_row][seen_col] != type
                            ):
                                seen.add((check_row, seen_col, "up"))
                            else:
                                break
                        for seen_col in range(check_col + 1, cols):
                            if untouched_grid[check_row][seen_col] == type and (
                                no_up_row or untouched_grid[up_row][seen_col] != type
                            ):
                                seen.add((check_row, seen_col, "up"))
                            else:
                                break
                        sides += 1

                    # right
                    right_col = check_col + 1
                    no_right_col = right_col >= cols
                    if (
                        no_right_col or untouched_grid[check_row][right_col] != type
                    ) and (check_row, check_col, "right") not in seen:
                        for seen_row in range(check_row - 1, -1, -1):
                            if untouched_grid[seen_row][check_col] == type and (
                                no_right_col
                                or untouched_grid[seen_row][right_col] != type
                            ):
                                seen.add((seen_row, check_col, "right"))
                            else:
                                break
                        for seen_row in range(check_row + 1, rows):
                            if untouched_grid[seen_row][check_col] == type and (
                                no_right_col
                                or untouched_grid[seen_row][right_col] != type
                            ):
                                seen.add((seen_row, check_col, "right"))
                            else:
                                break
                        sides += 1

                    # down
                    down_row = check_row + 1
                    no_down_row = down_row >= rows
                    if (
                        no_down_row or untouched_grid[down_row][check_col] != type
                    ) and (check_row, check_col, "down") not in seen:
                        for seen_col in range(check_col - 1, -1, -1):
                            if untouched_grid[check_row][seen_col] == type and (
                                no_down_row
                                or untouched_grid[down_row][seen_col] != type
                            ):
                                seen.add((check_row, seen_col, "down"))
                            else:
                                break
                        for seen_col in range(check_col + 1, cols):
                            if untouched_grid[check_row][seen_col] == type and (
                                no_down_row
                                or untouched_grid[down_row][seen_col] != type
                            ):
                                seen.add((check_row, seen_col, "down"))
                            else:
                                break
                        sides += 1

                    # left
                    left_col = check_col - 1
                    no_left_col = left_col < 0
                    if (
                        no_left_col or untouched_grid[check_row][left_col] != type
                    ) and (check_row, check_col, "left") not in seen:
                        for seen_row in range(check_row - 1, -1, -1):
                            if untouched_grid[seen_row][check_col] == type and (
                                no_left_col
                                or untouched_grid[seen_row][left_col] != type
                            ):
                                seen.add((seen_row, check_col, "left"))
                            else:
                                break
                        for seen_row in range(check_row + 1, rows):
                            if untouched_grid[seen_row][check_col] == type and (
                                no_left_col
                                or untouched_grid[seen_row][left_col] != type
                            ):
                                seen.add((seen_row, check_col, "left"))
                            else:
                                break
                        sides += 1

                return area * sides

            pt_1_res = 0
            pt_2_res = 0
            for row in range(rows):
                for col in range(cols):
                    v = grid[row][col]

                    if v != TOMBSTONE:
                        res = explore_region(row, col, v, rows, cols)
                        pt_1_res += res

                        res = explore_region_pt_2(row, col, v, rows, cols)

                        pt_2_res += res

            print(f"pt_1_res: {pt_1_res}")
            print(f"pt_2_res: {pt_2_res}")

            return (str(pt_1_res), str(pt_2_res))
