PT_1_BLINKS = 25
PT_2_BLINKS = 75

from collections import defaultdict
from os.path import join
from base.day import Day

class Day11(Day):
    def solve(self):
        pt_1_res = ""
        pt_2_res = ""

        with open(join("src", "d11", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            # vals: dict[int, int] = [(int(v), v, len(v)) for v in line.split(' ')]
            vals: dict[str, int] = defaultdict(int)
            for v in line.split(" "):
                vals[v] += 1

            for i in range(PT_2_BLINKS):
                new_vals: dict[str, int] = defaultdict(int)

                for k, v in vals.items():
                    if k == "0":
                        new_vals["1"] += v
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
                    pt_1_res = str(sum(vals.values()))

            pt_2_res = str(sum(vals.values()))

        return (pt_1_res, pt_2_res)
