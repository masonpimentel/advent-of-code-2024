from collections import deque
import sys
from os.path import join
from base.day import Day


class Day09(Day):
    def solve(self):
        with open(join("src", "d09", "input.txt"), encoding="utf-8") as f:
            input = f.readline()

            q: list[str] = deque()
            pt_2: list[int] = []

            ptr = 0
            max_id = 0
            for i, c in enumerate(input):
                if i % 2 == 0:
                    id = int(i) // 2
                    max_id = max(max_id, id)

                    repeat = int(c)
                    gap = int(input[i + 1]) if i < len(input) - 1 else 0

                    for _ in range(repeat):
                        q.append(id)
                        pt_2.append(id)
                        ptr += 1

                    for _ in range(gap):
                        q.append(".")
                        pt_2.append(".")
                        ptr += 1

            pt_1: list[str] = []
            while len(q) > 0:

                a_val = q.popleft()
                if a_val != ".":
                    pt_1.append(a_val)
                else:
                    pt_1.append(q.pop())

                while len(q) > 0 and q[-1] == ".":
                    q.pop()

            checksum_pt_1 = 0
            for i in range(len(pt_1)):
                checksum_pt_1 += pt_1[i] * i

            for id in range(max_id, -1, -1):
                first_idx = sys.maxsize
                last_idx = -sys.maxsize

                for i in range(len(pt_2)):
                    if pt_2[i] == id:
                        first_idx = min(first_idx, i)
                        last_idx = max(last_idx, i)

                streak_needed = last_idx - first_idx + 1
                streak_start = -1
                streak_count = 0
                for i in range(first_idx):
                    if pt_2[i] != ".":
                        streak_start = -1
                        streak_count = 0
                    else:
                        if streak_start == -1:
                            streak_start = i
                        streak_count += 1

                        if streak_count == streak_needed:
                            for set_i in range(
                                streak_start, streak_start + streak_count
                            ):
                                pt_2[set_i] = id

                            for set_i in range(first_idx, last_idx + 1):
                                pt_2[set_i] = "."

                            break

            checksum_pt_2 = 0
            for i in range(len(pt_2)):
                val = pt_2[i]

                checksum_pt_2 += val * i if val != "." else 0

            return (str(checksum_pt_1), str(checksum_pt_2))
