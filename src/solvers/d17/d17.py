"""Day 17"""

from re import search, findall
from typing import Literal, NamedTuple
from sys import maxsize
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class AttemptArgs(NamedTuple):
    """Args for attempt method"""

    instructions: list[int]
    a: int
    ins_idx: int
    ins_len: int
    orig_b: int
    orig_c: int


class Day17(Day):
    """Chronospatial Computer"""

    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        self.c = 0
        self.instructions: list[int] = []
        self.num_instructions = 0

    def combo_operand(self, combo: int) -> int:
        match combo:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c

        return combo

    def dv(self, operand: int, target: Literal["A", "B", "C"]) -> None:
        divisor = 2 ** self.combo_operand(operand)
        res = int(self.a / divisor)

        match target:
            case "A":
                self.a = res
            case "B":
                self.b = res
            case "C":
                self.c = res

    def run_program(self, a: int, b: int, c: int) -> list[int]:
        self.a = a
        self.b = b
        self.c = c

        ins_ptr = 0
        output: list[int] = []

        while ins_ptr < self.num_instructions:
            if ins_ptr == self.num_instructions - 1:
                print(
                    "Problem: cannot get operand because ins_ptr is at last instruction"
                )
                return []

            instruction = self.instructions[ins_ptr]
            operand = self.instructions[ins_ptr + 1]
            new_ins_ptr = ins_ptr + 2

            match instruction:
                case 0:
                    self.dv(operand, "A")
                case 6:
                    self.dv(operand, "B")
                case 7:
                    self.dv(operand, "C")
                case 1:
                    self.b = self.b ^ operand
                case 2:
                    self.b = self.combo_operand(operand) % 8
                case 3:
                    if self.a != 0:
                        new_ins_ptr = operand
                case 4:
                    self.b = self.b ^ self.c
                case 5:
                    output.append(self.combo_operand(operand) % 8)

            ins_ptr = new_ins_ptr

        return output

    def attempt(self, args: AttemptArgs) -> int:
        instructions, a, ins_idx, ins_len, orig_b, orig_c = args
        output = self.run_program(a, orig_b, orig_c)
        res = maxsize

        if len(output) >= ins_idx and instructions[-ins_idx] == output[-ins_idx]:
            if ins_idx == ins_len:
                return a

            for inc in range(8):
                # When you have a match on this output index
                # there are 8 more possible values that a can be
                rec_res = self.attempt(
                    AttemptArgs(
                        instructions,
                        (a * 8) + inc,
                        ins_idx + 1,
                        ins_len,
                        orig_b,
                        orig_c,
                    )
                )
                res = min(res, rec_res)

        return res

    def solve(self) -> SolveInfo:
        with open(get_path("17"), encoding="utf-8") as f:
            line = f.readline()
            if match := search(r"\d+", line):
                orig_a = int(match.group())
            else:
                orig_a = 0

            line = f.readline()
            if match := search(r"\d+", line):
                orig_b = int(match.group())
            else:
                orig_b = 0

            line = f.readline()
            if match := search(r"\d+", line):
                orig_c = int(match.group())
            else:
                orig_c = 0

            line = f.readline()
            line = f.readline()

            self.instructions = list(map(int, findall(r"\d+", line)))
            self.num_instructions = len(self.instructions)

        pt_1_res = ",".join(list(map(str, self.run_program(orig_a, orig_b, orig_c))))
        pt_2_res = maxsize

        for try_a in range(8):
            rec_res = self.attempt(
                AttemptArgs(
                    self.instructions, try_a, 1, len(self.instructions), orig_b, orig_c
                )
            )

            pt_2_res = min(pt_2_res, rec_res)

        return SolveInfo(pt_1_res, str(pt_2_res))
