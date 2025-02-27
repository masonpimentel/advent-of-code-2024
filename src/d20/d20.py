from sys import setrecursionlimit, maxsize

from os.path import join

class Day20:
    def solve(self):
        setrecursionlimit(10**6)

        with open(
            join('src', 'd20', 'input.txt'), encoding="utf-8"
        ) as f:
            grid: list[list[str]] = []

            line = f.readline()
            while line:
                row = [c for c in line]

                row = row[:-1] if row[-1] == '\n' else row[:] 
                grid.append(row)

                line = f.readline()


            rows = len(grid)
            cols = len(grid[0])

            dp: list[list[int]] = [[-1] * cols for _ in range(rows)]
            seen: list[list[bool]] = [[False] * cols for _ in range(rows)]
            
            def move(row: int, col: int, seen: list[tuple[int, int]], rows: int, cols: int) -> int:
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    return maxsize
                
                if grid[row][col] == '#':
                    return maxsize
                
                if seen[row][col]:
                    return maxsize
                
                if grid[row][col] == 'E':
                    dp[row][col] = 0
                    return 0

                
                if dp[row][col] != -1:
                    return dp[row][col]
                
                res = maxsize

                seen[row][col] = True
                for row_diff, col_diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    check_row = row + row_diff
                    check_col = col + col_diff

                    rec_res = move(check_row, check_col, seen, rows, cols)

                    res = min(res, 1 + rec_res)

                seen[row][col] = False
                dp[row][col] = res

                return res
            

            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 'S':
                        move(row, col, seen, rows, cols)

            pt_1_slots: set[tuple[int, int]] = set()
            PT_1_JUMP = 2
            for row in range(-PT_1_JUMP, PT_1_JUMP + 1):
                for col in range(-PT_1_JUMP, PT_1_JUMP + 1):
                    dist = abs(row) + abs(col)

                    if dist == PT_1_JUMP:
                        pt_1_slots.add((row, col))
            
            pt_2_slots: set[tuple[int, int, int]] = set()
            PT_2_JUMP = 20
            for row in range(-PT_2_JUMP, PT_2_JUMP + 1):
                for col in range(-PT_2_JUMP, PT_2_JUMP + 1):
                    dist = abs(row) + abs(col)

                    if dist <= PT_2_JUMP:
                        pt_2_slots.add((row, col, dist))

            THRESHOLD = 100
            pt_1_res = 0
            pt_2_res = 0
            for row in range(rows):
                for col in range(cols):
                    if dp[row][col] != -1:
                        for row_diff, col_diff in pt_1_slots:
                            check_row = row + row_diff
                            check_col = col + col_diff

                            if check_row < 0 or check_row >= rows or check_col < 0 or check_col >= cols:
                                continue

                            if dp[check_row][check_col] == -1:
                                continue

                            cheat_adv = dp[row][col] - dp[check_row][check_col] - PT_1_JUMP

                            if cheat_adv >= THRESHOLD:
                                pt_1_res += 1
                        
                        for row_diff, col_diff, jump in pt_2_slots:
                            check_row = row + row_diff
                            check_col = col + col_diff

                            if check_row < 0 or check_row >= rows or check_col < 0 or check_col >= cols:
                                continue

                            if dp[check_row][check_col] == -1:
                                continue

                            cheat_adv = dp[row][col] - dp[check_row][check_col] - jump

                            if cheat_adv >= THRESHOLD:
                                pt_2_res += 1
            
            print(f'pt_1_res: {pt_1_res}')
            print(f'pt_2_res: {pt_2_res}')

            return (str(pt_1_res), str(pt_2_res))


    