from os.path import join

class Day04:
    def solve(self):
        with open(
            join('src', 'd04', 'input.txt'), encoding="utf-8"
        ) as f:
            line = f.readline()

            mat: list[list[str]] = []

            while line:
                mat.append([c for c in line])

                line = f.readline()

                if line:
                    mat[-1] = mat[-1][:-1]
            
            rows = len(mat)
            cols = len(mat[0])

            def new_row_and_col(row: int, col: int, d: int) -> tuple[int, int]:
                new_row = row
                new_col = col
                match d:
                    case 0:
                        new_row = row - 1
                    case 1:
                        new_row = row - 1
                        new_col = col + 1
                    case 2:
                        new_col = col + 1
                    case 3:
                        new_row = row + 1
                        new_col = col + 1
                    case 4:
                        new_row = row + 1
                    case 5:
                        new_row = row + 1
                        new_col = col - 1
                    case 6:
                        new_col = col - 1
                    case 7:
                        new_row = row - 1
                        new_col = col - 1
                
                return (new_row, new_col)


            # dir
            # 0 = up
            # 1 = up-right
            # 2 = right
            # 3 = down-right
            # 4 = down
            # 5 = down-left
            # 6 = left
            # 7 = up-left
            def search(row: int, col: int, looking_for: str, dir: int) -> bool:
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    return False
                
                if mat[row][col] != looking_for:
                    return False
                
                new_row, new_col = new_row_and_col(row, col, dir)

                if looking_for == 'M':
                    return search(new_row, new_col, 'A', dir)
                elif looking_for == 'A':
                    return search(new_row, new_col, 'S', dir)
                else:
                    return True
                    

            def count_words(row: int, col: int) -> int:
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    return 0

                if mat[row][col] != 'X':
                    return 0
                
                res = 0
                for d in range(8):
                    new_row, new_col = new_row_and_col(row, col, d)

                    if search(new_row, new_col, 'M', d):
                        res += 1
                
                return res
            
            def part_one() -> str:
                res = 0
                for row in range(rows):
                    for col in range(cols):
                        res += count_words(row, col)


                print(f'pt_1_res: {res}')
                return str(res)
            

            def part_two() -> str:
                # MMMSXXMASM

                res = 0
                for row in range(rows - 2):
                    for col in range(cols - 2):
                        if mat[row + 1][col + 1] == 'A':
                            if (mat[row][col] == 'M' and mat[row][col + 2] == 'S' and mat[row + 2][col] == 'M' and mat[row + 2][col + 2] == 'S') or ((mat[row][col] == 'M' and mat[row][col + 2] == 'M' and mat[row + 2][col] == 'S' and mat[row + 2][col + 2] == 'S')) or ((mat[row][col] == 'S' and mat[row][col + 2] == 'M' and mat[row + 2][col] == 'S' and mat[row + 2][col + 2] == 'M')) or (mat[row][col] == 'S' and mat[row][col + 2] == 'S' and mat[row + 2][col] == 'M' and mat[row + 2][col + 2] == 'M'):
                                res += 1
                    
                print(f'pt_2_res: {res}')
                return str(res)

            pt1 = part_one()
            pt2 = part_two()

            return (pt1, pt2)
        


        # M S
        #  A
        # M S

        # M M
        #  A
        # S S

        # S M
        #  A
        # S M

        # S S
        #  A
        # M M