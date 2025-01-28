from re import search
from sys import maxsize

print(f'Runs in ~0.007 seconds')

with open(
    'input.txt', encoding="utf-8"
) as f:
    line = f.readline()


    # no_disabling_matches = findall(r'mul\((\d*),(\d*)\)', full_input)

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

    def cost(a_x: int, a_y: int, b_x: int, b_y: int, t_x: int, t_y: int, is_part_2: bool = False) -> int:        
        # a(a_x) + b(b_x) = t_x
        # a(a_y) + b(b_y) = t_y

        # a(a_x) = t_x - b(b_x)
        # a = (t_x - b(b_x)) / a_x
        # a_y((t_x - b(b_x)) / a_x) = t_y - b(b_y)
        # a_y(t_x - b(b_x) = t_y(a_x) - b(b_y)(a_x)
        # a_y(t_x) - a_y(b)(b_x) = t_y(a_x) - b(b_y)(a_x)
        # b(b_y)(a_x) - b(a_y)(b_x) = t_y(a_x) - a_y(t_x)
        # b((b_y)(a_x) - a_y(b_x)) = t_y(a_x) - a_y(t_x)
        # b = (t_y)(a_x) - (a_y)(t_x) / (b_y)(a_x) - (a_y)(b_x)

        if is_part_2:
            t_x += 10000000000000
            t_y += 10000000000000


        b = ((t_y * a_x) - (a_y * t_x)) / ((b_y * a_x) - (a_y * b_x))

        
        
        # b(b_x) = t_x - a(a_x)
        # b = (t_x - a(a_x)) / b_x
        # a(a_y) + (b_y(t_x - a(a_x)) / b_x) = t_y
        # a(a_y) + (b_y(t_x) - a(b_y)(a_x)) / b_x = t_y
        # (b_y(t_x) - a(b_y)(a_x)) / b_x = t_y - a(a_y)
        # b_y(t_x) - a(b_y)(a_x) = b_x(t_y) - b_x(a)(a_y)
        # b_x(a)(a_y) - a(b_y)(a_x) = b_x(t_y) - b_y(t_x)
        # a((b_x)(a_y) - (b_y)(a_x)) = b_x(t_y) - b_y(t_x)
        # a = (b_x)(t_y) - (b_y)(t_x) / (b_x)(a_y) - (b_y)(a_x)
        a = ((b_x * t_y) - (b_y * t_x)) / ((b_x * a_y) - (b_y * a_x))
        
        # Check if a and b are integers
        return int((a * 3) + b) if a % 1 == 0 and b % 1 == 0 else maxsize
            


    pt_1_res = 0
    pt_2_res = 0

    while line:
        a = search(r'Button A: X\+(\d*), Y\+(\d*)', line)
        a_x, a_y = int(a.group(1)), int(a.group(2))

        # print(f'a_x {a_x} a_y {a_y}')

        line = f.readline()

        b = search(r'Button B: X\+(\d*), Y\+(\d*)', line)
        b_x, b_y = int(b.group(1)), int(b.group(2))

        # print(f'b_x {b_x} b_y {b_y}')

        line = f.readline()

        target = search(r'Prize: X=(\d*), Y=(\d*)', line)
        t_x, t_y = int(target.group(1)), int(target.group(2))

        # print(f't_x {t_x} t_y {t_y}')

        line = f.readline()
        line = f.readline()
    
        res = cost(a_x, a_y, b_x, b_y, t_x, t_y)
        pt_1_res += res if res < maxsize else 0
        res_pt_2 = cost(a_x, a_y, b_x, b_y, t_x, t_y, True)
        pt_2_res += res_pt_2 if res_pt_2 < maxsize else 0
    
    print(f'pt_1_res: {pt_1_res}')
    print(f'pt_2_res: {pt_2_res}')