"""Day 13"""

from re import search
from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


class EquationParts(NamedTuple):
    """Equation components for each claw machine configuration"""

    a_x: int
    a_y: int
    b_x: int
    b_y: int
    t_x: int
    t_y: int


class Day13(Day):
    """Claw Contraption"""

    def calculate_cost(self, eqn: EquationParts, is_part_2: bool = False) -> int:
        a_x, a_y, b_x, b_y, t_x, t_y = eqn

        if is_part_2:
            t_x += 10000000000000
            t_y += 10000000000000

        # a(a_x) + b(b_x) = t_x # eqn 1
        # a(a_y) + b(b_y) = t_y # eqn 2

        # isolate a in eqn 1
        # a(a_x) + b(b_x) = t_x
        # a(a_x) = t_x - b(b_x)
        # a = (t_x - b(b_x)) / a_x

        # isolate a in eqn 2
        # a(a_y) + b(b_y) = t_y
        # a(a_y) = t_y - b(b_y)
        # a = (t_y - b(b_y)) / a_y

        # solve for b
        # (t_x - b(b_x)) / a_x = (t_y - b(b_y)) / a_y
        # a_y((t_x - b(b_x)) / a_x) = t_y - b(b_y)
        # a_y(t_x - b(b_x) = t_y(a_x) - b(b_y)(a_x)
        # a_y(t_x) - a_y(b)(b_x) = t_y(a_x) - b(b_y)(a_x)
        # b(b_y)(a_x) - b(a_y)(b_x) = t_y(a_x) - a_y(t_x)
        # b((b_y)(a_x) - a_y(b_x)) = t_y(a_x) - a_y(t_x)
        # b = (t_y)(a_x) - (a_y)(t_x) / (b_y)(a_x) - (a_y)(b_x)
        b = ((t_y * a_x) - (a_y * t_x)) / ((b_y * a_x) - (a_y * b_x))

        # isolate b in eqn 1
        # a(a_x) + b(b_x) = t_x
        # b(b_x) = t_x - a(a_x)
        # b = (t_x - a(a_x)) / b_x

        # isolate b in eqn 2
        # a(a_y) + b(b_y) = t_y
        # b(b_y) = t_y - a(a_y)
        # b = (t_y - a(a_y)) / b_y

        # solve for a
        # (t_x - a(a_x)) / b_x = (t_y - a(a_y)) / b_y
        # a(a_y) + (b_y(t_x - a(a_x)) / b_x) = t_y
        # a(a_y) + (b_y(t_x) - a(b_y)(a_x)) / b_x = t_y
        # (b_y(t_x) - a(b_y)(a_x)) / b_x = t_y - a(a_y)
        # b_y(t_x) - a(b_y)(a_x) = b_x(t_y) - b_x(a)(a_y)
        # b_x(a)(a_y) - a(b_y)(a_x) = b_x(t_y) - b_y(t_x)
        # a((b_x)(a_y) - (b_y)(a_x)) = b_x(t_y) - b_y(t_x)
        # a = (b_x)(t_y) - (b_y)(t_x) / (b_x)(a_y) - (b_y)(a_x)
        a = ((b_x * t_y) - (b_y * t_x)) / ((b_x * a_y) - (b_y * a_x))

        # Check if a and b are integers
        return int((a * 3) + b) if a % 1 == 0 and b % 1 == 0 else 0

    def solve(self) -> SolveInfo:
        with open(get_path("13"), encoding="utf-8") as f:
            line = f.readline()

            pt_1_res = 0
            pt_2_res = 0

            values: list[EquationParts] = []

            while line:
                a = search(r"Button A: X\+(\d*), Y\+(\d*)", line)
                if a:
                    a_x, a_y = int(a.group(1)), int(a.group(2))
                else:
                    a_x, a_y = 0, 0

                line = f.readline()

                b = search(r"Button B: X\+(\d*), Y\+(\d*)", line)
                if b:
                    b_x, b_y = int(b.group(1)), int(b.group(2))
                else:
                    b_x, b_y = 0, 0

                line = f.readline()

                target = search(r"Prize: X=(\d*), Y=(\d*)", line)
                if target:
                    t_x, t_y = int(target.group(1)), int(target.group(2))
                else:
                    t_x, t_y = 0, 0

                values.append(EquationParts(a_x, a_y, b_x, b_y, t_x, t_y))

                line = f.readline()
                line = f.readline()

        for a_x, a_y, b_x, b_y, t_x, t_y in values:
            pt_1_res += self.calculate_cost(EquationParts(a_x, a_y, b_x, b_y, t_x, t_y))
            pt_2_res += self.calculate_cost(
                EquationParts(a_x, a_y, b_x, b_y, t_x, t_y), True
            )

        return SolveInfo(str(pt_1_res), str(pt_2_res))
