from collections import defaultdict, deque
from re import search

import time

start = time.perf_counter()

def solve():
    print(f'Runs in ~0.004 seconds')

    with open(
        'input.txt', encoding="utf-8"
    ) as f:
        wire_tuples: list[tuple[str, int]] = []
        logic_tuples: list[tuple[int, int, int, int]] = []

        line = f.readline()
        while line:
            if line == '\n':
                break

            r = search(r'(\w*): (\d*)', line)
            wire_tuples.append((r.group(1), int(r.group(2) )))

            line = f.readline()

        line = f.readline()
        
        while line:
            r = search(r'(\w*) (\w*) (\w*) -> (\w*)', line)

            logic_tuples.append((r.group(1), r.group(2), r.group(3), r.group(4)))

            line = f.readline()

        def get_wire_num(wire: str) -> int:
            return int(wire[1:])

        x_max_bit = 0
        y_max_bit = 0
        z_max_bit = 0
        i = 0
        for wire1, gate, wire2, res_wire in logic_tuples:
            match wire1[0]:
                case 'x':
                    x_max_bit = max(x_max_bit, get_wire_num(wire1))
                case 'y':
                    y_max_bit = max(y_max_bit, get_wire_num(wire1))
                case 'z':
                    z_max_bit = max(z_max_bit, get_wire_num(wire1))

            match wire2[0]:
                case 'x':
                    x_max_bit = max(x_max_bit, get_wire_num(wire2))
                case 'y':
                    y_max_bit = max(y_max_bit, get_wire_num(wire2))
                case 'z':
                    z_max_bit = max(z_max_bit, get_wire_num(wire2))

            match res_wire[0]:
                case 'x':
                    x_max_bit = max(x_max_bit, get_wire_num(res_wire))
                case 'y':
                    y_max_bit = max(y_max_bit, get_wire_num(res_wire))
                case 'z':
                    z_max_bit = max(z_max_bit, get_wire_num(res_wire))
        

        if x_max_bit != y_max_bit or x_max_bit != z_max_bit - 1:
            print('There is a problem with the bit counts')
            return

        z_bits = z_max_bit + 1

        wires: defaultdict[str, int] = defaultdict(lambda: -1)

        for wire, val in wire_tuples:
            wires[wire] = val

        q: list[tuple[str, str, str, str]] = deque(logic_tuples)
        
        cur_zs = 0
        q_count = 0
        while len(q) > 0:
            # print(q)
            wire1, gate, wire2, res_wire = q.popleft()

            q_count += 1

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
            
                if cur_zs == z_bits:
                    break
        

            # print(wires)
        
        b = ''
        for i in range(z_bits - 1, -1, -1):
            wire = f"z{'0' if i < 10 else ''}{i}"
            b += str(wires[wire])

        z = int(b, 2)

        



        pt_2_set: set[str] = set()

        NON_TEMP_BITS = ['x', 'y', 'z']
        for wire1, gate, wire2, res_wire in logic_tuples:
            wire1_first = wire1[0]
            wire2_first = wire2[0]
            res_wire_first = res_wire[0]

            # check 1:
            # the outputs of an "AND" must be "ORed"

            # correct:
            #     pgm
            #         AND  jmf
            #     rqm
            #                  OR
            #              
            #              ppf

            # incorrect:
            #     pgm
            #         AND  jmf
            #     rqm
            #                  XOR
            #              
            #              ppf
            if gate == 'AND' and wire1[1:] != '00' and wire2[1:] != '00':
                for next_wire1, next_gate, next_wire2, _ in logic_tuples:
                    if (next_wire1 == res_wire or next_wire2 == res_wire) and next_gate != 'OR':
                        pt_2_set.add(res_wire)
            
            
            if gate == 'XOR':
                for next_wire1, next_gate, next_wire2, _ in logic_tuples:
                    # check 2
                    # the outputs of an "XOR" cannot be "ORed"

                    # correct:
                    #              dpb    
                    # 
                    #                  XOR
                    #     x05
                    #         XOR  wgk
                    #     y05

                    # correct:
                    #              dpb    
                    # 
                    #                  OR
                    #     x05
                    #         XOR  wgk
                    #     y05
                    if (next_wire1 == res_wire or next_wire2 == res_wire) and next_gate == 'OR':
                        pt_2_set.add(res_wire)

                # check 3
                # cannot have all wires in an XOR a temp bit

                # correct:
                #     dpb
                #         AND  jwp
                #     wgk

                # incorrect:
                #     dpb
                #         XOR  jwp
                #     wgk
                if wire1_first not in NON_TEMP_BITS and wire2_first not in NON_TEMP_BITS and res_wire_first not in NON_TEMP_BITS:
                    pt_2_set.add(res_wire)

            
            if res_wire_first == 'z' and res_wire[1:] != str(z_max_bit):
                # check 4
                # the gate for a z wire must be XOR

                # correct:
                #     mjw
                #         XOR  z40
                #     bvt

                # incorrect:
                #     rqt
                #         AND  z23
                #     rdt
                if gate != 'XOR':
                    pt_2_set.add(res_wire)
            


        print(f'pt_1_res: {z}')
        print(f'pt_2_res: {",".join([str(v) for v in sorted(list(pt_2_set))])}')



                    
    end = time.perf_counter()
    s = (end-start)
    print(f"Elapsed {s:.03f} seconds")

solve()