from sys import maxsize

DIRECTION_PAD_ROWS = 2
DIRECTION_PAD_COLS = 3

direction_pad = [
    ['X', '^', 'A'],
    ['<', 'v', '>']
]

human_to_direction_dp = {}

def human_to_direction(row: int, col: int, dst: str, seen: set[str]) -> tuple[str, int, int, int]:
    if row < 0 or row >= DIRECTION_PAD_ROWS or col < 0 or col >= DIRECTION_PAD_COLS:
        return ('', maxsize, row, col)
    
    seen_tpl = (row, col)
    if seen_tpl in seen:
        return ('', maxsize, row, col)
    
    if direction_pad[row][col] == 'X':
        return ('', maxsize, row, col)

    if direction_pad[row][col] == dst:
        return ('A', 1, row, col)
    
    best_distance = maxsize
    seq = ''
    res_row = -1
    res_col = -1

    seen.add(seen_tpl)
    for row_diff, col_diff, input in [(-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<')]:
        check_row = row + row_diff
        check_col = col + col_diff
        rec_res = human_to_direction(check_row, check_col, dst, seen)

        this_seq = input + rec_res[0]
        this_dis = 1 + rec_res[1]

        if this_dis < best_distance:
            best_distance = this_dis
            seq = this_seq
            res_row = rec_res[2]
            res_col = rec_res[3]
    
    seen.remove(seen_tpl)
    return (seq, best_distance, res_row, res_col)

NUMBER_PAD_ROWS = 4
NUMBER_PAD_COLS = 3

number_pad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['X', '0', 'A'],
]

direction_to_keypad_dp = {}

def direction_to_keypad(row: int, col: int, dst: str, seen: set[str]) -> tuple[str, int, int, int]:
    if row < 0 or row >= NUMBER_PAD_ROWS or col < 0 or col >= NUMBER_PAD_COLS:
        return ('', maxsize, row, col)
    
    seen_tpl = (row, col)
    if seen_tpl in seen:
        return ('', maxsize, row, col)
    
    if number_pad[row][col] == 'X':
        return ('', maxsize, row, col)

    if number_pad[row][col] == dst:
        return ('A', 1, row, col)
    
    best_distance = maxsize
    seq = ''
    res_row = -1
    res_col = -1

    seen.add(seen_tpl)
    for row_diff, col_diff, input in [(-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<')]:
        check_row = row + row_diff
        check_col = col + col_diff
        rec_res = direction_to_keypad(check_row, check_col, dst, seen)

        this_seq = input + rec_res[0]
        this_dis = 1 + rec_res[1]

        if this_dis < best_distance:
            best_distance = this_dis
            seq = this_seq
            res_row = rec_res[2]
            res_col = rec_res[3]
    
    seen.remove(seen_tpl)
    return (seq, best_distance, res_row, res_col)

direction_to_direction_dp = {}

def direction_to_direction(row: int, col: int, dst: str, seen: set[str]) -> tuple[str, int, int, int]:
    if row < 0 or row >= DIRECTION_PAD_ROWS or col < 0 or col >= DIRECTION_PAD_COLS:
        return ('', maxsize, row, col)
    
    seen_tpl = (row, col)
    if seen_tpl in seen:
        return ('', maxsize, row, col)
    
    if direction_pad[row][col] == 'X':
        return ('', maxsize, row, col)

    if direction_pad[row][col] == dst:
        return ('A', 1, row, col)
    
    best_distance = maxsize
    seq = ''
    res_row = -1
    res_col = -1

    seen.add(seen_tpl)
    for row_diff, col_diff, input in [(-1, 0, '^'), (0, 1, '>'), (1, 0, 'v'), (0, -1, '<')]:
        check_row = row + row_diff
        check_col = col + col_diff
        rec_res = direction_to_direction(check_row, check_col, dst, seen)

        this_seq = input + rec_res[0]
        this_dis = 1 + rec_res[1]

        if this_dis < best_distance:
            best_distance = this_dis
            seq = this_seq
            res_row = rec_res[2]
            res_col = rec_res[3]
    
    seen.remove(seen_tpl)
    return (seq, best_distance, res_row, res_col)

dir_1_row = 0
dir_1_col = 2
dir_2_row = 0
dir_2_col = 2
key_row = 3
key_col = 2



codes: list[str] = []

with open(
    'input.txt', encoding="utf-8"
) as f:
    line = f.readline()


    while line:
        code = [c for c in line]

        codes.append(code[:-1] if code[-1] == '\n' else code)

        line = f.readline()

for code in codes:
    seq = ''

    for c in code:
        dir_2_seq, _, key_row, key_col = direction_to_keypad(key_row, key_col, c, set())

        # print(f'keypad_res {keypad_res}')

        for dst_2 in dir_2_seq:
            # print(f'dir_2_res {dir_2_res} dst {dst_2}, start row {dir_2_row}, start col {dir_2_col}')

            dir_1_seq, _, dir_2_row, dir_2_col = direction_to_direction(dir_2_row, dir_2_col, dst_2, set())

            for dst_1 in dir_1_seq:
                human_seq, _, dir_1_row, dir_1_col = human_to_direction(dir_1_row, dir_1_col, dst_1, set())

                seq += human_seq

    # <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

    print(code)
    print(seq)
    print(len(seq))
    print(f'pt_1_res: TODO')
    print(f'pt_2_res: TODO')


        


# print(r)

    
