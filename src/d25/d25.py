from os.path import join


class Day25:
    def solve(self):
        with open(join("src", "d25", "input.txt"), encoding="utf-8") as f:
            self.keys: list[list[int]] = []
            self.locks: list[list[int]] = []

            self.cur_ob: list[list[str]] = []

            def add_ob():
                if len(self.cur_ob) != 7:
                    print("Found an ob with height != 7")

                is_lock = True
                for c in self.cur_ob[0]:
                    if c != "#":
                        is_lock = False
                        break

                width = len(self.cur_ob[0])
                if is_lock:
                    new_lock = [0] * width
                    for row in self.cur_ob:
                        for i, c in enumerate(row):
                            if c == "#":
                                new_lock[i] += 1

                    self.locks.append(list(map(lambda x: x - 1, new_lock)))
                else:
                    new_key = [0] * width
                    for row in self.cur_ob[::-1]:
                        for i, c in enumerate(row):
                            if c == "#":
                                new_key[i] += 1

                    self.keys.append(list(map(lambda x: x - 1, new_key)))

                self.cur_ob = []

            line = f.readline()
            while line:
                if line == "\n":
                    add_ob()
                else:
                    row = line[:-1] if line[-1] == "\n" else line[:]
                    self.cur_ob.append(row)

                line = f.readline()

            add_ob()

        pt_1_res = 0
        for key in self.keys:
            for lock in self.locks:
                fits = True

                if len(key) != len(lock):
                    print(f"Key and lock with mismatching lengths")

                for i in range(len(lock)):
                    if lock[i] + key[i] > 5:
                        fits = False
                        break

                if fits:
                    pt_1_res += 1

        print(f"pt_1_res: {pt_1_res}")
        print(f"pt_2_res: NO_PT_2")

        return (str(pt_1_res), "NO_PT_2")
