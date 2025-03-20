"""Day 3"""

from re import findall
from os.path import join
from base.day import Day

# pylint: disable=R0903
class Day03(Day):
    """Day 3 solver"""

    def get_res(self, input_str: str) -> str:
        res = 0

        matches = findall(r"mul\((\d*),(\d*)\)", input_str)
        for v1, v2 in matches:
            res += int(v1) * int(v2)

        return str(res)

    def solve(self) -> tuple[str, str]:
        pt_1_res = ""
        pt_2_res = ""
        is_add = True
        seq: list[str] = []

        with open(join("src", "d03", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                for i, c in enumerate(line):
                    pt_1_res += c

                    if line[i : i + 7] == "don't()":
                        is_add = False

                    if "".join(seq[-4:]) == "do()":
                        is_add = True
                        seq = seq[:-4]

                    if is_add:
                        pt_2_res += c

                    seq.append(c)

                line = f.readline()

        return (str(self.get_res(pt_1_res)), str(self.get_res(pt_2_res)))
