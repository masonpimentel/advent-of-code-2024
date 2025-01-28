from collections import defaultdict, deque
from re import search

import time

start = time.perf_counter()

with open(
    'input.txt', encoding="utf-8"
) as f:
    

    wires: dict[str, int] = defaultdict(lambda: -1)

    line = f.readline()
    while line:
        if line == '\n':
            break

        r = search(r'(\w*): (\d*)', line)

        wire, val = r.group(1), r.group(2) 

        # print(f'wire {wire} val {val}')
        wires[wire] = int(val)


        line = f.readline()
    

    q: list[tuple[str, str, str, str]] = deque()

    line = f.readline()
    
    while line:
        # ntg XOR fgs -> mjb
        r = search(r'(\w*) (\w*) (\w*) -> (\w*)', line)

        q.append((r.group(1), r.group(2), r.group(3), r.group(4)))

        line = f.readline()

    z_count = 0
    outputs: list[str] = []
    i = 0
    for wire1, gate, wire2, res_wire in q:
        max_z = -1

        if res_wire[0] == 'z':
            max_z = max(max_z, int(res_wire[1:]))

        z_count = max(z_count, max_z + 1)

        outputs.append(res_wire)

        i += 1
    
    # print(f'z_count {z_count}')
    
    cur_zs = 0
    while len(q) > 0:
        wire1, gate, wire2, res_wire = q.popleft()

        if wires[wire1] < 0 or wires[wire2] < 0:
            q.append((wire1, wire2, gate, res_wire))
            # print(f'needed {wire1} and {wire2}')
            continue

        match gate:
            case 'AND':
                wires[res_wire] = 1 if wires[wire1] == 1 and wires[wire2] == 1 else 0
            case 'OR':
                wires[res_wire] = 1 if wires[wire1] == 1 or wires[wire2] == 1 else 0
            case 'XOR':
                # if res_wire == 'z09':
                    # print(f'wire1 {wire1} wire2 {wire2} 1 if wires[wire1] != wires[wire2] else 0 {1 if wires[wire1] != wires[wire2] else 0}')
                wires[res_wire] = 1 if wires[wire1] != wires[wire2] else 0
        
        if res_wire[0] == 'z':
            cur_zs += 1
        
            if cur_zs == z_count:
                break
    

        # print(wires)
    
    b = ''
    for i in range(z_count - 1, -1, -1):
        z = f"z{'0' if i < 10 else ''}{i}"
        # print(f'looking for {z}, {wires[z]}')
        b += str(wires[z])
    
    print(f'pt_1_res: {int(b, 2)}')
    print(f'pt_2_res: TODO')

    # 0, 1, 3, 17
    # 0, 2, 7, 9
    # 19, 3, 4, 7

    # def attempt(swaps: list[int]) -> bool:
        

    # outputs_count = len(outputs) 
    # for i in range(outputs_count):
    #     for j in range(outputs_count):
    #         if j == i:
    #             continue
    #         for k in range(outputs_count):
    #             if k == i or k == j:
    #                 continue
    #             for l in range(outputs_count):
    #                 if l == i or l == j or l == k:
    #                     continue

                
end = time.perf_counter()
s = (end-start)
print(f"Elapsed {s:.03f} seconds")