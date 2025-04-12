"""Day 21"""

from sys import maxsize
from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=C0115
class SequenceInfo(NamedTuple):
    sequence: str
    move_count: int


class Day21(Day):
    """Keypad Conundrum"""

    NUMBER_PAD = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["X", "0", "A"],
    ]
    NUMBER_PAD_ROWS = len(NUMBER_PAD)
    NUMBER_PAD_COLS = len(NUMBER_PAD[0])

    DIRECTION_PAD = [["X", "^", "A"], ["<", "v", ">"]]

    DIRECTION_PAD_ROWS = len(DIRECTION_PAD)
    DIRECTION_PAD_COLS = len(DIRECTION_PAD[0])

    MOVE_DELTAS = [
        (-1, 0, "^"),
        (0, 1, ">"),
        (1, 0, "v"),
        (0, -1, "<"),
    ]

    def __init__(self) -> None:
        self.dp: dict[str, dict[str, int]] = {}
        self.dir_pad_dp: dict[int, dict[str, dict[str, SequenceInfo]]] = {}
        self.dir_pad_same_level_dp: dict[str, dict[str, list[SequenceInfo]]] = {}

        self.row_col_from_num_pad = {
            self.NUMBER_PAD[row][col]: (row, col)
            for row in range(self.NUMBER_PAD_ROWS)
            for col in range(self.NUMBER_PAD_COLS)
        }
        self.row_col_from_dir_pad = {
            self.DIRECTION_PAD[row][col]: (row, col)
            for row in range(self.DIRECTION_PAD_ROWS)
            for col in range(self.DIRECTION_PAD_COLS)
        }

    # pylint: disable=R0914
    def dir_pad_same_level(
        self, src: str, dst: str, seen: set[str]
    ) -> list[SequenceInfo]:
        if src in seen or src == "X":
            return [SequenceInfo("", maxsize)]

        if src == dst:
            return [SequenceInfo("A", 1)]

        seen.add(src)

        src_row, src_col = self.row_col_from_dir_pad[src]

        possible_this_level: list[SequenceInfo] = []

        for row_diff, col_diff, pad_input in self.MOVE_DELTAS:
            check_row = src_row + row_diff
            check_col = src_col + col_diff

            if (
                check_row < 0
                or check_row >= self.DIRECTION_PAD_ROWS
                or check_col < 0
                or check_col >= self.DIRECTION_PAD_COLS
            ):
                continue

            this_move_dst = self.DIRECTION_PAD[check_row][check_col]

            this_layer_res = self.dir_pad_same_level(this_move_dst, dst, seen)

            for this_layer_seq, this_layer_dist in this_layer_res:
                if this_layer_dist < maxsize:
                    possible_this_level.append(
                        SequenceInfo(pad_input + this_layer_seq, 1 + this_layer_dist)
                    )

        seen.remove(src)

        return possible_this_level

    # pylint: disable=R0914,R0912
    def dir_pad_all_levels(
        self, src: str, dst: str, level: int, human_level: int
    ) -> SequenceInfo:
        if level not in self.dir_pad_dp:
            self.dir_pad_dp[level] = {}
        if src not in self.dir_pad_dp[level]:
            self.dir_pad_dp[level][src] = {}
        if dst in self.dir_pad_dp[level][src]:
            return self.dir_pad_dp[level][src][dst]

        if level == human_level:
            return SequenceInfo(dst, 1)

        if src == "X":
            return SequenceInfo("", maxsize)

        if src == dst:
            return SequenceInfo("A", 1)

        if src not in self.dir_pad_same_level_dp:
            self.dir_pad_same_level_dp[src] = {}
        if dst in self.dir_pad_same_level_dp[src]:
            possible_this_level = self.dir_pad_same_level_dp[src][dst]
        else:
            possible_this_level = self.dir_pad_same_level(src, dst, set())
            self.dir_pad_same_level_dp[src][dst] = possible_this_level

        best_distance = maxsize
        seq = ""

        for this_layer_seq, _ in possible_this_level:
            lower_layers_seq = ""
            lower_layers_dist = 0

            for i, lower_dst in enumerate(this_layer_seq):
                lower_level = level + 1

                if i == 0:
                    lower_src = "A"
                    lower_layers_res = self.dir_pad_all_levels(
                        "A", this_layer_seq[i], lower_level, human_level
                    )
                else:
                    lower_src = this_layer_seq[i - 1]

                if (
                    lower_level in self.dir_pad_dp
                    and lower_src in self.dir_pad_dp[lower_level]
                    and lower_dst in self.dir_pad_dp[lower_level][lower_src]
                ):
                    lower_layers_res = self.dir_pad_dp[lower_level][lower_src][
                        lower_dst
                    ]
                else:
                    lower_layers_res = self.dir_pad_all_levels(
                        lower_src, lower_dst, lower_level, human_level
                    )

                lower_layers_seq, lower_layers_dist = (
                    "",
                    lower_layers_dist + lower_layers_res[1],
                )

            if lower_layers_dist < best_distance:
                best_distance = lower_layers_dist
                seq = lower_layers_seq

        r = SequenceInfo(seq, best_distance)
        self.dir_pad_dp[level][src][dst] = r
        return r

    # pylint: disable=R0914
    def number_pad_possible(
        self, src: str, dst: str, seen: set[str]
    ) -> list[SequenceInfo]:
        if src in seen or src == "X":
            return [SequenceInfo("", maxsize)]

        if src == dst:
            return [SequenceInfo("A", 1)]

        seen.add(src)

        src_row, src_col = self.row_col_from_num_pad[src]

        possible_this_level: list[SequenceInfo] = []

        for row_diff, col_diff, pad_input in self.MOVE_DELTAS:
            check_row = src_row + row_diff
            check_col = src_col + col_diff

            if (
                check_row < 0
                or check_row >= self.NUMBER_PAD_ROWS
                or check_col < 0
                or check_col >= self.NUMBER_PAD_COLS
            ):
                continue

            this_move_dst = self.NUMBER_PAD[check_row][check_col]

            this_layer_res = self.number_pad_possible(this_move_dst, dst, seen)

            for this_layer_seq, this_layer_dist in this_layer_res:
                if this_layer_dist < maxsize:
                    possible_this_level.append(
                        SequenceInfo(pad_input + this_layer_seq, 1 + this_layer_dist)
                    )

        seen.remove(src)

        return possible_this_level

    def number_pad_press(self, src: str, dst: str, levels: int) -> int:
        if src not in self.dp:
            self.dp[src] = {}
        if dst in self.dp[src]:
            return self.dp[src][dst]

        possible_ways = self.number_pad_possible(src, dst, set())

        best_distance = maxsize

        for this_layer_seq, _ in possible_ways:
            lower_layers_seq = ""
            lower_layers_dist = 0

            for i, lower_dst in enumerate(this_layer_seq):
                if i == 0:
                    lower_src = "A"
                else:
                    lower_src = this_layer_seq[i - 1]

                if (
                    1 in self.dir_pad_dp
                    and lower_src in self.dir_pad_dp[1]
                    and lower_dst in self.dir_pad_dp[1][lower_src]
                ):
                    lower_layers_res = self.dir_pad_dp[1][lower_src][lower_dst]
                else:
                    lower_layers_res = self.dir_pad_all_levels(
                        lower_src, lower_dst, 1, levels
                    )

                lower_layers_seq, lower_layers_dist = (
                    lower_layers_seq + lower_layers_res[0],
                    lower_layers_dist + lower_layers_res[1],
                )

            best_distance = min(best_distance, lower_layers_dist)

        self.dp[src][dst] = best_distance
        return best_distance

    def get_for_complexity(self, direction_keypad_count: int) -> str:
        self.dp = {}
        self.dir_pad_dp = {}
        self.dir_pad_same_level_dp = {}
        codes: list[str] = []

        with open(get_path("21"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                codes.append(line[:-1] if line[-1] == "\n" else line)

                line = f.readline()

        res = 0
        for code in codes:
            l = 0
            for i, cur_c in enumerate(code):
                if i == 0:
                    l += self.number_pad_press("A", code[i], direction_keypad_count)
                else:
                    l += self.number_pad_press(
                        code[i - 1], cur_c, direction_keypad_count
                    )

            numeric_of_code = int("".join(code[:-1]))
            res += l * numeric_of_code

        return str(res)

    def solve(self) -> SolveInfo:
        pt_1_res = self.get_for_complexity(3)
        pt_2_res = self.get_for_complexity(26)

        return SolveInfo(pt_1_res, pt_2_res)
