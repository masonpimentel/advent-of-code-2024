print(f'Runs in ~0.116 seconds')

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

    res_pt_1: list[list[int]] = [[False] * cols for _ in range(rows)]
    res_pt_2: list[list[int]] = [[False] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '.':
                for scan_row in range(rows):
                    for scan_col in range(cols):
                        if scan_row == row and scan_col == col:
                            continue

                        if grid[scan_row][scan_col] == grid[row][col]:
                            row_diff = scan_row - row
                            col_diff = scan_col - col

                            anti_row_pt_1 = scan_row + row_diff
                            anti_col_pt_1 = scan_col + col_diff

                            if anti_row_pt_1 < rows and anti_row_pt_1 >= 0 and anti_col_pt_1 < cols and anti_col_pt_1 >= 0:
                                res_pt_1[anti_row_pt_1][anti_col_pt_1] = res_pt_1[anti_row_pt_1][anti_col_pt_1] or True

                            anti_row_pt2 = row
                            anti_col_pt2 = col

                            while anti_row_pt2 < rows and anti_row_pt2 >= 0 and anti_col_pt2 < cols and anti_col_pt2 >= 0:
                                res_pt_2[anti_row_pt2][anti_col_pt2] = res_pt_2[anti_row_pt2][anti_col_pt2] or True

                                anti_row_pt2 += row_diff
                                anti_col_pt2 += col_diff

    pt_1_res = 0
    for row in res_pt_1:
        for v in row:
            pt_1_res += 1 if v else 0
    pt_2_res = 0
    for row in res_pt_2:
        for v in row:
            pt_2_res += 1 if v else 0
    
    print(f'pt_1_res: {pt_1_res}')
    print(f'pt_2_res: {pt_2_res}')