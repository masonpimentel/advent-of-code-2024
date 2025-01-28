print(f'Runs in ~63.187 (!!) seconds')

with open(
    'input.txt', encoding="utf-8"
) as f:
    line = f.readline()

    grid: list[list[str]] = []

    while line:
        row = [c for c in line]

        if row[-1] == '\n':
            row = row[:-1]

        grid.append(row)

        line = f.readline()

    rows = len(grid)
    cols = len(grid[0])

    orig_grid: list[list[str]] = []
    for row in range(rows):
        orig_grid.append(grid[row][:])

    row_pos = -1
    col_pos = -1
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '^':
                row_pos = row
                col_pos = col
    
    row_cannot = row_pos
    col_cannot = col_pos
    direc = 'up'

    positions: list[list[str]] = [['.'] * cols for _ in range(rows)]    

    def run_simulation(row_pos: int, col_pos: int, direc: str, set_positions: bool) -> bool:
        seen = {}

        while True:
            if row_pos in seen and col_pos in seen[row_pos] and direc in seen[row_pos][col_pos]:
                return True

            if set_positions:
                positions[row_pos][col_pos] = 'V'
            new_row = row_pos
            new_col = col_pos
            new_direc = direc
            match direc:
                case 'up':
                    if row_pos == 0:
                        break

                    if grid[row_pos - 1][col_pos] == '#':
                        new_direc = 'right'
                    else:
                        new_row -= 1
                case 'right':
                    if col_pos == cols - 1:
                        break

                    if grid[row_pos][col_pos + 1] == '#':
                        new_direc = 'down'
                    else:
                        new_col += 1
                case 'down':
                    if row_pos == rows - 1:
                        break
                
                    if grid[row_pos + 1][col_pos] == '#':
                        new_direc = 'left'
                    else:
                        new_row += 1
                case 'left':
                    if col_pos == 0:
                        break

                    if grid[row_pos][col_pos - 1] == '#':
                        new_direc = 'up'
                    else:
                        new_col -= 1

            if row_pos not in seen:
                seen[row_pos] = {}
            if col_pos not in seen[row_pos]:
                seen[row_pos][col_pos] = set()
            seen[row_pos][col_pos].add(direc)

            row_pos = new_row
            col_pos = new_col
            direc = new_direc
        
        return False
    
    run_simulation(row_pos, col_pos, direc, True)
    pt_1_res = 0
    pt_2_res = 0
    for row in range(rows):
        for col in range(cols):
            if positions[row][col] == 'V':
                pt_1_res += 1
            
            if grid[row][col] == '.' and (row != row_cannot or col != col_cannot):
                grid[row][col] = '#'
                res = run_simulation(row_pos, col_pos, direc, False)
                if res:
                    pt_2_res += 1
                grid[row][col] = '.'
    
    print(f'pt_1_res: {pt_1_res}')
    print(f'pt_2_res: {pt_2_res}')
                