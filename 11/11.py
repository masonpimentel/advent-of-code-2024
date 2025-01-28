PT_1_BLINKS = 25
PT_2_BLINKS = 75

from collections import defaultdict

print(f'Runs in ~0.226 seconds')

with open(
    'input.txt', encoding="utf-8"
) as f:
    line = f.readline()

    # vals: dict[int, int] = [(int(v), v, len(v)) for v in line.split(' ')]
    vals: dict[str, int] = defaultdict(int)
    for v in line.split(' '):
        vals[v] += 1


    for i in range(PT_2_BLINKS):
        new_vals: dict[str, int] = defaultdict(int)

        for k, v in vals.items():
            if k == '0':
                new_vals['1'] += v
            elif len(k) % 2 == 0:
                l = len(k)
                split = l // 2

                left = int(k[:split])
                right = int(k[split:])
                
                new_vals[str(left)] += v
                new_vals[str(right)] += v
            else:
                new_int = int(k) * 2024
                new_vals[str(new_int)] += v
        
        vals = new_vals

        if i == PT_1_BLINKS - 1:
            print(f'pt_1_res: {sum(vals.values())}')
    
    print(f'pt_2_res: {sum(vals.values())}')

