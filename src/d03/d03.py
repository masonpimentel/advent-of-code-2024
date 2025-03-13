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
        full_input = ""
        disabling_input = ""
        is_add = True
        seq: list[str] = []

        with open(join("src", "d03", "input.txt"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                for i, c in enumerate(line):
                    full_input += c

                    if line[i : i + 7] == "don't()":
                        is_add = False

                    if "".join(seq[-4:]) == "do()":
                        is_add = True
                        seq = seq[:-4]

                    if is_add:
                        disabling_input += c

                    seq.append(c)

                line = f.readline()

        return (str(self.get_res(full_input)), str(self.get_res(disabling_input)))
