"""Day 24"""

from collections import defaultdict, deque
from re import search
from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=C0115
class WireState(NamedTuple):
    wire: str
    state: int


class Gate(NamedTuple):
    """Logic gate components"""

    wire_1: str
    wire_2: str
    gate: str
    res_wire: str


class Day24(Day):
    """Crossed Wires"""

    def __init__(self) -> None:
        self.wires: list[WireState] = []
        self.gates: list[Gate] = []
        self.z_max_bit = 0

    def get_z_max_bit(self) -> int:
        def get_wire_num(wire: str) -> int:
            return int(wire[1:])

        x_max_bit = 0
        y_max_bit = 0
        z_max_bit = 0
        for wire1, _, wire2, res_wire in self.gates:
            match wire1[0]:
                case "x":
                    x_max_bit = max(x_max_bit, get_wire_num(wire1))
                case "y":
                    y_max_bit = max(y_max_bit, get_wire_num(wire1))
                case "z":
                    z_max_bit = max(z_max_bit, get_wire_num(wire1))

            match wire2[0]:
                case "x":
                    x_max_bit = max(x_max_bit, get_wire_num(wire2))
                case "y":
                    y_max_bit = max(y_max_bit, get_wire_num(wire2))
                case "z":
                    z_max_bit = max(z_max_bit, get_wire_num(wire2))

            match res_wire[0]:
                case "x":
                    x_max_bit = max(x_max_bit, get_wire_num(res_wire))
                case "y":
                    y_max_bit = max(y_max_bit, get_wire_num(res_wire))
                case "z":
                    z_max_bit = max(z_max_bit, get_wire_num(res_wire))

        if x_max_bit != y_max_bit or x_max_bit != z_max_bit - 1:
            print("There is a problem with the bit counts")
            return -1

        return z_max_bit

    def get_pt_1(self) -> str:
        z_bits = self.z_max_bit + 1

        wire_lookup: defaultdict[str, int] = defaultdict(lambda: -1)

        for wire, val in self.wires:
            wire_lookup[wire] = val

        q: deque[Gate] = deque(self.gates)

        cur_zs = 0
        q_count = 0
        while len(q) > 0:
            wire1, gate, wire2, res_wire = q.popleft()

            q_count += 1

            if wire_lookup[wire1] < 0 or wire_lookup[wire2] < 0:
                q.append(Gate(wire1, wire2, gate, res_wire))
                continue

            match gate:
                case "AND":
                    wire_lookup[res_wire] = (
                        1 if wire_lookup[wire1] == 1 and wire_lookup[wire2] == 1 else 0
                    )
                case "OR":
                    wire_lookup[res_wire] = (
                        1 if wire_lookup[wire1] == 1 or wire_lookup[wire2] == 1 else 0
                    )
                case "XOR":
                    wire_lookup[res_wire] = (
                        1 if wire_lookup[wire1] != wire_lookup[wire2] else 0
                    )

            if res_wire[0] == "z":
                cur_zs += 1

                if cur_zs == z_bits:
                    break

        b = ""
        for i in range(z_bits - 1, -1, -1):
            wire = f"z{'0' if i < 10 else ''}{i}"
            b += str(wire_lookup[wire])

        return str(int(b, 2))

    def get_pt_2(self) -> str:
        issues: set[str] = set()

        non_temp_bits = ["x", "y", "z"]
        for wire1, gate, wire2, res_wire in self.gates:
            wire1_first = wire1[0]
            wire2_first = wire2[0]
            res_wire_first = res_wire[0]

            # check 1:
            # the outputs of an "AND" must be "ORed"

            # correct:
            #     pgm
            #         AND  jmf
            #     rqm
            #                  OR
            #
            #              ppf

            # incorrect:
            #     pgm
            #         AND  jmf
            #     rqm
            #                  XOR
            #
            #              ppf
            if gate == "AND" and wire1[1:] != "00" and wire2[1:] != "00":
                for next_wire1, next_gate, next_wire2, _ in self.gates:
                    if (res_wire in (next_wire1, next_wire2)) and next_gate != "OR":
                        issues.add(res_wire)

            if gate == "XOR":
                for next_wire1, next_gate, next_wire2, _ in self.gates:
                    # check 2
                    # the outputs of an "XOR" cannot be "ORed"

                    # correct:
                    #              dpb
                    #
                    #                  XOR
                    #     x05
                    #         XOR  wgk
                    #     y05

                    # incorrect:
                    #              dpb
                    #
                    #                  OR
                    #     x05
                    #         XOR  wgk
                    #     y05
                    if (res_wire in (next_wire1, next_wire2)) and next_gate == "OR":
                        issues.add(res_wire)

                # check 3
                # cannot have all wires in an XOR a temp bit

                # correct:
                #     dpb
                #         AND  jwp
                #     wgk

                # incorrect:
                #     dpb
                #         XOR  jwp
                #     wgk
                if (
                    wire1_first not in non_temp_bits
                    and wire2_first not in non_temp_bits
                    and res_wire_first not in non_temp_bits
                ):
                    issues.add(res_wire)

            if res_wire_first == "z" and res_wire[1:] != str(self.z_max_bit):
                # check 4
                # the gate for a z wire must be XOR

                # correct:
                #     mjw
                #         XOR  z40
                #     bvt

                # incorrect:
                #     rqt
                #         AND  z23
                #     rdt
                if gate != "XOR":
                    issues.add(res_wire)

        return ",".join([str(v) for v in sorted(list(issues))])

    def solve(self) -> SolveInfo:
        self.wires = []
        self.gates = []

        with open(get_path("24"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                if line == "\n":
                    break

                r = search(r"(\w*): (\d*)", line)
                if r:
                    self.wires.append(WireState(r.group(1), int(r.group(2))))

                line = f.readline()

            line = f.readline()

            while line:
                r = search(r"(\w*) (\w*) (\w*) -> (\w*)", line)

                if r:
                    self.gates.append(
                        Gate(r.group(1), r.group(2), r.group(3), r.group(4))
                    )

                line = f.readline()

        self.z_max_bit = self.get_z_max_bit()

        if self.z_max_bit == -1:
            return SolveInfo("", "")

        return SolveInfo(self.get_pt_1(), self.get_pt_2())
