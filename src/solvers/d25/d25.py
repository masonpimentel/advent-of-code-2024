"""Day 25"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class Day25(Day):
    """Code Chronicle"""

    def __init__(self) -> None:
        self.keys: list[list[int]] = []
        self.locks: list[list[int]] = []

    def add(self, key_or_lock: list[list[str]]) -> None:
        if len(key_or_lock) != 7:
            print("Found an ob with height != 7")

        is_lock = True
        for c in key_or_lock[0]:
            if c != "#":
                is_lock = False
                break

        width = len(key_or_lock[0])
        if is_lock:
            new_lock = [0] * width
            for row in key_or_lock:
                for i, c in enumerate(row):
                    if c == "#":
                        new_lock[i] += 1

            self.locks.append(list(map(lambda x: x - 1, new_lock)))
        else:
            new_key = [0] * width
            for row in key_or_lock[::-1]:
                for i, c in enumerate(row):
                    if c == "#":
                        new_key[i] += 1

            self.keys.append(list(map(lambda x: x - 1, new_key)))

    def solve(self) -> SolveInfo:
        self.keys = []
        self.locks = []
        key_or_locks: list[list[list[str]]] = []
        cur_key_or_lock: list[list[str]] = []

        with open(get_path("25"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                if line == "\n":
                    key_or_locks.append(cur_key_or_lock)
                    cur_key_or_lock = []
                else:
                    row = line[:-1] if line[-1] == "\n" else line[:]
                    cur_key_or_lock.append(list(row))

                line = f.readline()

            key_or_locks.append(cur_key_or_lock)

        for key_or_lock in key_or_locks:
            self.add(key_or_lock)

        pt_1_res = 0
        for key in self.keys:
            for lock in self.locks:
                fits = True

                if len(key) != len(lock):
                    print("Key and lock with mismatching lengths")

                for i, lock_row in enumerate(lock):
                    if lock_row + key[i] > 5:
                        fits = False
                        break

                if fits:
                    pt_1_res += 1

        return SolveInfo(str(pt_1_res), "NO_PT_2")
