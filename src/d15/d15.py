import sys

from os.path import join

class Day15:
    def solve(self):
        print(f'Runs in ~0.084 seconds')

        with open(
            join('src', 'd15', 'input.txt'), encoding="utf-8"
        ) as f:
            grid_pt_1: list[list[str]] = []
            grid_pt_2: list[list[str]] = []

            line = f.readline()

            while line:
                if line == '\n':
                    break

                row = [c for c in line]
                row = row[:-1]

                grid_pt_1.append(row)

                row_pt_2 = []
                for c in row:
                    match c:
                        case '#':
                            row_pt_2.extend(['#', '#'])
                        case 'O':
                            row_pt_2.extend(['[', ']'])
                        case '@':
                            row_pt_2.extend(['@', '.'])
                        case '.':
                            row_pt_2.extend(['.', '.'])
                
                grid_pt_2.append(row_pt_2)


                line = f.readline()
            
            moves: list[str] = []

            line = f.readline()

            while line:
                row = [c for c in line]

                for move in row:
                    if move != '\n':
                        moves.append(move)
                
                line = f.readline()
            



            def compaction_pt_1(row: int, col: int, dir: str, rows: int, cols: int) -> tuple[int, int]:
                
                to_move = -1
                can_move = False
                if dir == '>':
                    for i in range(col + 1, cols - 1):
                        if grid_pt_1[row][i] == '.':
                            can_move = True
                            break
                        elif grid_pt_1[row][i] == '#':
                            break
                        else:
                            to_move = i
                
                    if can_move:
                        grid_pt_1[row][col] = '.'
                        grid_pt_1[row][col + 1] = '@'
                        if to_move > -1:
                            grid_pt_1[row][to_move + 1] = 'O'
                        
                        return (row, col + 1)
                elif dir == 'v':
                    for i in range(row + 1, rows - 1):
                        if grid_pt_1[i][col] == '.':
                            can_move = True
                            break
                        elif grid_pt_1[i][col] == '#':
                            break
                        else:
                            to_move = i
                
                    if can_move:
                        grid_pt_1[row][col] = '.'
                        grid_pt_1[row + 1][col] = '@'
                        if to_move > -1:
                            grid_pt_1[to_move + 1][col] = 'O'
                        
                        return (row + 1, col)
                elif dir == '<':
                    for i in range(col - 1, 0, -1):
                        if grid_pt_1[row][i] == '.':
                            can_move = True
                            break
                        elif grid_pt_1[row][i] == '#':
                            break
                        else:
                            to_move = i
                
                    if can_move:
                        grid_pt_1[row][col] = '.'
                        grid_pt_1[row][col - 1] = '@'
                        if to_move > -1:
                            grid_pt_1[row][to_move - 1] = 'O'
                        
                        return (row, col - 1)
                elif dir == '^':
                    for i in range(row - 1, 0, -1):
                        if grid_pt_1[i][col] == '.':
                            can_move = True
                            break
                        elif grid_pt_1[i][col] == '#':
                            break
                        else:
                            to_move = i
                
                    if can_move:
                        grid_pt_1[row][col] = '.'
                        grid_pt_1[row - 1][col] = '@'
                        if to_move > -1:
                            grid_pt_1[to_move - 1][col] = 'O'
                        
                        return (row - 1, col)


                
                return (row, col)
            
            def compaction_pt_1(row: int, col: int, dir: str, rows: int, cols: int) -> tuple[int, int]:                
                to_move = -1
                can_move = False
                if dir == '>':
                    for i in range(col + 1, cols - 1):
                        if grid_pt_1[row][i] == '.':
                            can_move = True
                            break
                        elif grid_pt_1[row][i] == '#':
                            break
                        else:
                            to_move = i
                
                    if can_move:
                        grid_pt_1[row][col] = '.'
                        grid_pt_1[row][col + 1] = '@'
                        if to_move > -1:
                            grid_pt_1[row][to_move + 1] = 'O'
                        
                        return (row, col + 1)
                elif dir == 'v':
                    for i in range(row + 1, rows - 1):
                        if grid_pt_1[i][col] == '.':
                            can_move = True
                            break
                        elif grid_pt_1[i][col] == '#':
                            break
                        else:
                            to_move = i
                
                    if can_move:
                        grid_pt_1[row][col] = '.'
                        grid_pt_1[row + 1][col] = '@'
                        if to_move > -1:
                            grid_pt_1[to_move + 1][col] = 'O'
                        
                        return (row + 1, col)
                elif dir == '<':
                    for i in range(col - 1, 0, -1):
                        if grid_pt_1[row][i] == '.':
                            can_move = True
                            break
                        elif grid_pt_1[row][i] == '#':
                            break
                        else:
                            to_move = i
                
                    if can_move:
                        grid_pt_1[row][col] = '.'
                        grid_pt_1[row][col - 1] = '@'
                        if to_move > -1:
                            grid_pt_1[row][to_move - 1] = 'O'
                        
                        return (row, col - 1)
                elif dir == '^':
                    for i in range(row - 1, 0, -1):
                        if grid_pt_1[i][col] == '.':
                            can_move = True
                            break
                        elif grid_pt_1[i][col] == '#':
                            break
                        else:
                            to_move = i
                
                    if can_move:
                        grid_pt_1[row][col] = '.'
                        grid_pt_1[row - 1][col] = '@'
                        if to_move > -1:
                            grid_pt_1[to_move - 1][col] = 'O'
                        
                        return (row - 1, col)


                
                return (row, col)
            
            def compaction_pt_2(row: int, col: int, dir: str, rows: int, cols: int) -> tuple[int, int]:
                def push_row(row: int, cols_prev_row: set[int], dir: str) -> bool:
                    new_cols: set[int] = set()
                    for check_col in cols_prev_row:
                        if grid_pt_2[row][check_col] == '#':
                            return False
                        
                        if grid_pt_2[row][check_col] == '[' or grid_pt_2[row][check_col] == ']':
                            new_cols.add(check_col)

                            if grid_pt_2[row][check_col] == '[':
                                
                                new_cols.add(check_col + 1)
                            else:
                                new_cols.add(check_col - 1)


                    prev_row = row + (1 if dir == '^' else -1)
                    if len(new_cols) == 0:                        
                        for set_col in cols_prev_row:
                            grid_pt_2[row][set_col] = grid_pt_2[prev_row][set_col]
                            grid_pt_2[prev_row][set_col] = '.'
                            
                        return True

                    old_row = grid_pt_2[row][:]

                    rec_res = push_row(row + (-1 if dir == '^' else 1), new_cols, dir)

                    if not rec_res:
                        grid_pt_2[row] = old_row
                        return False
                    else:
                        for set_col in cols_prev_row:
                            grid_pt_2[row][set_col] = grid_pt_2[prev_row][set_col]
                            grid_pt_2[prev_row][set_col] = '.'
                        return True
                
                to_remove = -1
                if dir == '>':
                    for i in range(col + 1, cols - 1):
                        if grid_pt_2[row][i] == '.':
                            to_remove = i
                            break
                        elif grid_pt_2[row][i] == '#':
                            break
                
                    if to_remove > -1:
                        grid_pt_2[row] = grid_pt_2[row][:col] + ['@'] + grid_pt_2[row][col:to_remove] + grid_pt_2[row][to_remove + 1:]
                        grid_pt_2[row][col] = '.'
                        
                        return (row, col + 1)
                elif dir == 'v':
                    res = push_row(row + 1, set([col]), dir)

                    if res:
                        grid_pt_2[row][col] = '.'
                        return (row + 1, col)
                elif dir == '<':
                    for i in range(col - 1, 0, -1):
                        if grid_pt_2[row][i] == '.':
                            to_remove = i
                            break
                        elif grid_pt_2[row][i] == '#':
                            break
                
                    if to_remove > -1:
                        # 
                        grid_pt_2[row] = grid_pt_2[row][:to_remove] + grid_pt_2[row][to_remove + 1:col] + ['@'] + grid_pt_2[row][col:]
                        grid_pt_2[row][col] = '.'
                        
                        return (row, col - 1)
                elif dir == '^':
                    res = push_row(row - 1, set([col]), dir)

                    if res:
                        grid_pt_2[row][col] = '.'
                        return (row - 1, col)

                
                return (row, col)
            
            rows_pt_1 = len(grid_pt_1)
            cols_pt_1 = len(grid_pt_1[0])

            for row in range(rows_pt_1):
                for col in range(cols_pt_1):
                    if grid_pt_1[row][col] == '@':
                        cur_row = row
                        cur_col = col
            
            rows_pt_2 = len(grid_pt_2)
            cols_pt_2 = len(grid_pt_2[0])

            for row in range(rows_pt_2):
                for col in range(cols_pt_2):
                    if grid_pt_2[row][col] == '@':
                        cur_row_pt_2 = row
                        cur_col_pt_2 = col
            
            for move in moves:
                cur_row, cur_col = compaction_pt_1(cur_row, cur_col, move, rows_pt_1, cols_pt_1)
                cur_row_pt_2, cur_col_pt_2 = compaction_pt_2(cur_row_pt_2, cur_col_pt_2, move, rows_pt_2, cols_pt_2)

            pt_1_res = 0
            for row in range(rows_pt_1):
                for col in range(cols_pt_1):
                    if grid_pt_1[row][col] == 'O':
                        pt_1_res += (100 * row) + col

            pt_2_res = 0
            for row in range(rows_pt_2):
                for col in range(cols_pt_2):
                    if grid_pt_2[row][col] == '[':
                        inc = (100 * row) + col
                        pt_2_res += inc


            print(f'pt_1_res: {pt_1_res}')
            print(f'pt_2_res: {pt_2_res}')
        
        return (str(pt_1_res), str(pt_2_res))
            
            # print(moves)
