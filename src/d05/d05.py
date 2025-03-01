from collections import defaultdict, Counter

from os.path import join


class Day05:
    def solve(self):
        with open(join("src", "d05", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            banned_lookup: dict[int, int] = defaultdict(list)
            process: list[list[int]] = []

            i = 1
            while line:
                if len(line) > 2:
                    if line[2] == "|":
                        dep_arr = line.split("|")
                        banned, val = int(dep_arr[0]), int(dep_arr[1])

                        banned_lookup[val].append(banned)
                    else:
                        process.append([int(c) for c in line.split(",")])

                line = f.readline()
                i += 1

            part_1 = 0
            part_2 = 0
            for i, to_process in enumerate(process):
                is_valid = True

                banned: set[int] = set()
                for val in to_process:
                    val_int = int(val)

                    if val_int in banned:
                        is_valid = False

                    for to_ban in banned_lookup[val_int]:
                        banned.add(int(to_ban))

                mid_idx = len(to_process) // 2
                if is_valid:
                    part_1 += to_process[mid_idx]
                else:
                    c = Counter(to_process)
                    s = set(c.keys())

                    new_order: list[int] = []
                    while len(s) > 0:
                        to_choose = None
                        for v in s:
                            is_valid = True
                            for other_v in s:
                                if v == other_v:
                                    continue

                                if other_v in banned_lookup[v]:
                                    is_valid = False
                                    continue
                            if is_valid:
                                to_choose = v
                        new_order += [to_choose] * c[to_choose]
                        s.remove(to_choose)

                    part_2 += new_order[mid_idx]

            print(f"pt_1_res: {part_1}")
            print(f"pt_2_res: {part_2}")

            return (str(part_1), str(part_2))
