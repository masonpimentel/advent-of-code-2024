"""Day 9"""

from collections import deque
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=R0903
class Block:
    """Part 2: Blocks which can be within Slots"""

    def __init__(self, block_id: int, size: int) -> None:
        self.id = block_id
        self.size = size


class Slot:
    """Part 2: Slots of memory"""

    def __init__(self, free: int = 0, block: Block | None = None) -> None:
        self._free = free
        self._blocks: list[Block] = [block] if block else []

    @property
    def free(self) -> int:
        return self._free

    @property
    def blocks(self) -> list[Block]:
        return self._blocks

    def has_free(self, size: int) -> bool:
        return self._free >= size

    def fill(self, block: Block) -> None:
        self._free -= block.size
        self._blocks.append(block)

    def clear(self) -> None:
        if self._blocks:
            self._free += self._blocks[0].size
            self._blocks.clear()


class Day09(Day):
    """Disk Fragmenter"""

    def get_pt_1(self, dq: deque[str]) -> str:
        blocks: list[str] = []

        while len(dq) > 0:
            a_val = dq.popleft()
            if a_val != ".":
                blocks.append(a_val)
            else:
                blocks.append(dq.pop())

            while len(dq) > 0 and dq[-1] == ".":
                dq.pop()

        res = 0
        for i, block in enumerate(blocks):
            res += int(block) * i

        return str(res)

    def get_pt_2(self, slots: list[Slot]) -> str:
        l = len(slots)
        for id_idx in range(l - 2, -1, -2):
            block_slot = slots[id_idx]
            block = block_slot.blocks[0]
            for space_idx in range(1, id_idx, 2):
                space_slot = slots[space_idx]
                if space_slot.has_free(block.size):
                    space_slot.fill(block)
                    block_slot.clear()
                    break

        res = 0
        ptr = 0
        for slot in slots:
            for block in slot.blocks:
                for _ in range(block.size):
                    to_add = block.id * ptr
                    res += to_add
                    ptr += 1

            for _ in range(slot.free):
                ptr += 1

        return str(res)

    def solve(self) -> SolveInfo:
        with open(get_path("09"), encoding="utf-8") as f:
            line = f.readline()

            pt_1_dq: deque[str] = deque()
            pt_2_slots: list[Slot] = []

            for i, c in enumerate(line):
                if i % 2 == 0:
                    block_id = int(i) // 2

                    repeat = int(c)
                    gap = int(line[i + 1]) if i < len(line) - 1 else 0

                    for _ in range(repeat):
                        pt_1_dq.append(str(block_id))

                    for _ in range(gap):
                        pt_1_dq.append(".")

                    pt_2_slots.append(Slot(0, Block(block_id, repeat)))
                    pt_2_slots.append(Slot(gap))

        pt_1_res = self.get_pt_1(pt_1_dq)
        pt_2_res = self.get_pt_2(pt_2_slots)

        return SolveInfo(str(pt_1_res), str(pt_2_res))
