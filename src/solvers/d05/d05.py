"""Day 5"""

from collections import defaultdict, Counter
from solvers.base.day import Day
from solvers.base.types import SolveInfo, RowCol
from solvers.utils.helpers import get_path


class Day05(Day):
    """Print Queue"""

    def get_pt_2_add(
        self, page_list: list[int], banned_lookup: dict[int, list[int]], mid_idx: int
    ) -> int:
        count = Counter(page_list)
        s = set(count.keys())

        new_order: list[int] = []
        while len(s) > 0:
            to_choose = -1
            for v in s:
                is_valid = True
                for other_v in s:
                    if v == other_v:
                        continue

                    if other_v in banned_lookup[v]:
                        is_valid = False
                        break
                if is_valid:
                    to_choose = v
            new_order += [to_choose] * count[to_choose]
            s.remove(to_choose)

        return new_order[mid_idx]

    def get_pt_1_pt_2_res(
        self, page_list: list[int], banned_lookup: dict[int, list[int]]
    ) -> RowCol:
        pt_1_add = 0
        pt_2_add = 0
        is_valid = True

        banned: set[int] = set()
        for val in page_list:
            val_int = int(val)

            if val_int in banned:
                is_valid = False

            for to_ban in banned_lookup[val_int]:
                banned.add(int(to_ban))

        mid_idx = len(page_list) // 2
        if is_valid:
            pt_1_add += page_list[mid_idx]
        else:
            pt_2_add += self.get_pt_2_add(page_list, banned_lookup, mid_idx)

        return RowCol(pt_1_add, pt_2_add)

    def solve(self) -> SolveInfo:
        with open(get_path("05"), encoding="utf-8") as f:
            line = f.readline()

            banned_lookup: dict[int, list[int]] = defaultdict(list)
            page_lists: list[list[int]] = []

            while line:
                if len(line) > 2:
                    if line[2] == "|":
                        dep_arr = line.split("|")
                        banned, val = int(dep_arr[0]), int(dep_arr[1])

                        banned_lookup[val].append(banned)
                    else:
                        page_lists.append([int(c) for c in line.split(",")])

                line = f.readline()

        pt_1_res = 0
        pt_2_res = 0
        for page_list in page_lists:
            adds = self.get_pt_1_pt_2_res(page_list, banned_lookup)
            pt_1_res += adds[0]
            pt_2_res += adds[1]

        return SolveInfo(str(pt_1_res), str(pt_2_res))
