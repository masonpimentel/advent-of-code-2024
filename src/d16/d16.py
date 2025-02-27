from collections import deque
from heapq import heappop, heappush

from os.path import join

class Day16:
    def solve(self):
        with open(
            join('src', 'd16', 'input.txt'), encoding="utf-8"
        ) as f:
            line = f.readline()

            grid: list[list[str]] = []

            while line:
                row = [c for c in line]
                grid.append(row[:-1] if row[-1] == '\n' else row)

                line = f.readline()

            rows = len(grid)
            cols = len(grid[0])

            start_tpl = None
            end_tpl = None

            for row in range(rows):
                if start_tpl != None and end_tpl != None:
                    break

                for col in range(cols):
                    if grid[row][col] == 'S':
                        start_tpl = (row, col)
                    elif grid[row][col] == 'E':
                        end_tpl = (row, col)

                    
                    if start_tpl != None and end_tpl != None:
                        break

            from_start: list[list[list[int]]] = [[[-1] * 4 for _ in range(cols)] for _ in range(rows)]

            # (point cost, row_diff, col_diff, new direction)
            # 0 = North, 1 = East, 2 = South, 3 = West
            new_positions: dict[str, list[tuple[int, int, int, int]]] = {
                0: [
                    (1, -1, 0, 0),
                    (1000, 0, 0, 1),
                    (2000, 0, 0, 2),
                    (1000, 0, 0, 3)
                ],
                1: [
                    (1000, 0, 0, 0),
                    (1, 0, 1, 1),
                    (1000, 0, 0, 2),
                    (2000, 0, 0, 3)
                ],
                2: [
                    (2000, 0, 0, 0),
                    (1000, 0, 0, 1),
                    (1, 1, 0, 2),
                    (1000, 0, 0, 3)
                ],
                3: [
                    (1000, 0, 0, 0),
                    (2000, 0, 0, 1),
                    (1000, 0, 0, 2),
                    (1, 0, -1, 3)
                ],
            }

            flip: dict[int, int] = {
                0: 2,
                1: 3,
                2: 0,
                3: 1
            }

            start_row, start_col = start_tpl[0], start_tpl[1]
            end_row, end_col = end_tpl[0], end_tpl[1]

            h: list[tuple[int, int, int, int]] = [(0, start_row, start_col, 1)]

            while len(h) > 0:
                dist, cur_row, cur_col, d = heappop(h)

                if cur_row < 0 or cur_row >= rows or cur_col < 0 or cur_col >= cols:
                    continue

                if from_start[cur_row][cur_col][d] > -1 or grid[cur_row][cur_col] == '#':
                    continue

                from_start[cur_row][cur_col][d] = dist

                for cost, row_diff, col_diff, new_dir in new_positions[d]:
                    heappush(h, (dist + cost, cur_row + row_diff, cur_col + col_diff, new_dir))

            from_back_h: list[tuple[int, int, int, str]] = [(0, end_row, end_col, start_d) for start_d in [0, 1, 2, 3]]
            from_back: list[list[list[int]]] = [[[-1] * 4 for _ in range(cols)] for _ in range(rows)]
            path: list[list[int]] = [[0] * cols for _ in range(rows)]

            while len(from_back_h) > 0:
                dist, cur_row, cur_col, d = heappop(from_back_h)

                if cur_row < 0 or cur_row >= rows or cur_col < 0 or cur_col >= cols:
                    continue

                if from_back[cur_row][cur_col][d] > -1 or grid[cur_row][cur_col] == '#':
                    continue

                from_back[cur_row][cur_col][d] = dist

                for cost, row_diff, col_diff, new_dir in new_positions[d]:
                    heappush(from_back_h, (dist + cost, cur_row + row_diff, cur_col + col_diff, new_dir))

            from_start_total = min(from_start[end_row][end_col])
            for row in range(rows):
                for col in range(cols):
                    for d in [0, 1, 2, 3]:
                        if from_back[row][col][d] == from_start_total - from_start[row][col][flip[d]]:
                            path[row][col] = 1
                            break
            
            pt_2_res = 0
            for row in path:
                pt_2_res += sum(row)

            pt_1_res = min(from_start[end_tpl[0]][end_tpl[1]])

            print(f'pt_1_res: {pt_1_res}')
            print(f'pt_2_res: {pt_2_res}')
        
            return (str(pt_1_res), str(pt_2_res))
