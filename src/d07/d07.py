from os.path import join


class Day07:
    def __init__(self):
        self.pt_1_res = ""
        self.pt_2_res = ""

    def solve(self):
        with open(join("src", "d07", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            def rec(tot: int, cur: int, vals: list[int]) -> bool:
                if len(vals) == 0:
                    return tot == cur

                # add
                if rec(tot, cur + vals[0], vals[1:]):
                    return True
                # mul
                if rec(tot, cur * vals[0], vals[1:]):
                    return True

                return False

            pt_1_res = 0
            i = 0
            while line:
                tot, vals = line.split(": ")

                tot = int(tot)
                vals = list(map(lambda x: int(x), vals.split(" ")))

                if rec(tot, vals[0], vals[1:]):
                    pt_1_res += tot

                line = f.readline()
                i += 1

            self.pt_1_res = str(pt_1_res)
            print(f"pt_1_res: {pt_1_res}")

        with open(join("src", "d07", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            def rec(tot: int, cur: int, vals: list[int]) -> bool:
                if len(vals) == 0:
                    return tot == cur

                # add
                if rec(tot, cur + vals[0], vals[1:]):
                    return True
                # mul
                if rec(tot, cur * vals[0], vals[1:]):
                    return True
                # combine
                if rec(tot, int(str(cur) + str(vals[0])), vals[1:]):
                    return True

                return False

            pt_2_res = 0
            i = 0
            while line:
                tot, vals = line.split(": ")

                tot = int(tot)
                vals = list(map(lambda x: int(x), vals.split(" ")))

                if rec(tot, vals[0], vals[1:]):
                    pt_2_res += tot

                line = f.readline()
                i += 1

            self.pt_2_res = str(pt_2_res)
            print(f"pt_2_res: {pt_2_res}")

        return (self.pt_1_res, self.pt_2_res)
