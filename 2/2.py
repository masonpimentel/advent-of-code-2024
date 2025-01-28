print(f'Runs in ~0.012 seconds')

def check_line(vals: list[int]) -> bool:
    is_safe = True

    is_increase = vals[1] > vals[0]
    for i in range(len(vals) - 1):
        diff = abs(vals[i + 1] - vals[i])
        if diff < 1 or diff > 3:
            is_safe = False
            break

        if is_increase and vals[i + 1] <= vals[i]:
            is_safe = False
            break
        if not is_increase and vals[i + 1] >= vals[i]:
            is_safe = False
            break
    
    return is_safe


with open(
    'input.txt', encoding="utf-8"
) as f:
    line = f.readline()

    safe_no_dampener = 0
    safe_with_dampener = 0
    while line:
        vals = list(map(lambda v: int(v), line.split(' ')))

        orig_result = check_line(vals)
        
        if orig_result:
            safe_no_dampener += 1
            safe_with_dampener += 1
        else:
            for i in range(len(vals)):
                line_with_i_removed = check_line(vals[:i] + vals[i + 1:])
                if line_with_i_removed:
                    safe_with_dampener += 1
                    break


        line = f.readline()
    
    print(f'pt_1_res: {safe_no_dampener}')
    print(f'pt_2_res: {safe_with_dampener}')