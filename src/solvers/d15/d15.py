"""Day 15"""

from solvers.base.day import Day
from solvers.base.types import SolveInfo, RowCol
from solvers.utils.helpers import get_path


class Day15(Day):
    """Warehouse Woes"""

    def __init__(self) -> None:
        self.grid_pt_1: list[list[str]] = []
        self.grid_pt_2: list[list[str]] = []
        self.moves: list[str] = []
        self.rows_pt_1 = -1
        self.cols_pt_1 = -1
        self.rows_pt_2 = -1
        self.cols_pt_2 = -1

    def right_pt_1(self, row: int, col: int) -> RowCol:
        to_move = -1
        can_move = False
        for i in range(col + 1, self.cols_pt_1 - 1):
            if self.grid_pt_1[row][i] == ".":
                can_move = True
                break
            if self.grid_pt_1[row][i] == "#":
                break

            to_move = i

        if can_move:
            self.grid_pt_1[row][col] = "."
            self.grid_pt_1[row][col + 1] = "@"
            if to_move > -1:
                self.grid_pt_1[row][to_move + 1] = "O"

            return RowCol(row, col + 1)

        return RowCol(row, col)

    def left_pt_1(self, row: int, col: int) -> RowCol:
        to_move = -1
        can_move = False
        for i in range(col - 1, 0, -1):
            if self.grid_pt_1[row][i] == ".":
                can_move = True
                break
            if self.grid_pt_1[row][i] == "#":
                break

            to_move = i

        if can_move:
            self.grid_pt_1[row][col] = "."
            self.grid_pt_1[row][col - 1] = "@"
            if to_move > -1:
                self.grid_pt_1[row][to_move - 1] = "O"

            return RowCol(row, col - 1)

        return RowCol(row, col)

    def down_pt_1(self, row: int, col: int) -> RowCol:
        to_move = -1
        can_move = False
        for i in range(row + 1, self.rows_pt_1 - 1):
            if self.grid_pt_1[i][col] == ".":
                can_move = True
                break
            if self.grid_pt_1[i][col] == "#":
                break

            to_move = i

        if can_move:
            self.grid_pt_1[row][col] = "."
            self.grid_pt_1[row + 1][col] = "@"
            if to_move > -1:
                self.grid_pt_1[to_move + 1][col] = "O"

            return RowCol(row + 1, col)

        return RowCol(row, col)

    def up_pt_1(self, row: int, col: int) -> RowCol:
        to_move = -1
        can_move = False
        for i in range(row - 1, 0, -1):
            if self.grid_pt_1[i][col] == ".":
                can_move = True
                break
            if self.grid_pt_1[i][col] == "#":
                break

            to_move = i

        if can_move:
            self.grid_pt_1[row][col] = "."
            self.grid_pt_1[row - 1][col] = "@"
            if to_move > -1:
                self.grid_pt_1[to_move - 1][col] = "O"

            return RowCol(row - 1, col)

        return RowCol(row, col)

    def compaction_pt_1(self, row: int, col: int, direc: str) -> RowCol:
        match direc:
            case ">":
                return self.right_pt_1(row, col)
            case "<":
                return self.left_pt_1(row, col)
            case "^":
                return self.up_pt_1(row, col)
            case "v":
                return self.down_pt_1(row, col)

        return RowCol(row, col)

    def push_row(self, row: int, cols_prev_row: set[int], direc: str) -> bool:
        new_cols: set[int] = set()
        for check_col in cols_prev_row:
            if self.grid_pt_2[row][check_col] == "#":
                return False

            if (
                self.grid_pt_2[row][check_col] == "["
                or self.grid_pt_2[row][check_col] == "]"
            ):
                new_cols.add(check_col)

                if self.grid_pt_2[row][check_col] == "[":
                    new_cols.add(check_col + 1)
                else:
                    new_cols.add(check_col - 1)

        prev_row = row + (1 if direc == "^" else -1)
        if len(new_cols) == 0:
            for set_col in cols_prev_row:
                self.grid_pt_2[row][set_col] = self.grid_pt_2[prev_row][set_col]
                self.grid_pt_2[prev_row][set_col] = "."

            return True

        old_row = self.grid_pt_2[row][:]

        rec_res = self.push_row(row + (-1 if direc == "^" else 1), new_cols, direc)

        if not rec_res:
            self.grid_pt_2[row] = old_row
            return False

        for set_col in cols_prev_row:
            self.grid_pt_2[row][set_col] = self.grid_pt_2[prev_row][set_col]
            self.grid_pt_2[prev_row][set_col] = "."
        return True

    def right_pt_2(self, row: int, col: int) -> RowCol:
        to_remove = -1
        for i in range(col + 1, self.cols_pt_2 - 1):
            if self.grid_pt_2[row][i] == ".":
                to_remove = i
                break
            if self.grid_pt_2[row][i] == "#":
                break

        if to_remove > -1:
            self.grid_pt_2[row] = (
                self.grid_pt_2[row][:col]
                + ["@"]
                + self.grid_pt_2[row][col:to_remove]
                + self.grid_pt_2[row][to_remove + 1 :]
            )
            self.grid_pt_2[row][col] = "."

            return RowCol(row, col + 1)

        return RowCol(row, col)

    def left_pt_2(self, row: int, col: int) -> RowCol:
        to_remove = -1
        for i in range(col - 1, 0, -1):
            if self.grid_pt_2[row][i] == ".":
                to_remove = i
                break
            if self.grid_pt_2[row][i] == "#":
                break

        if to_remove > -1:
            self.grid_pt_2[row] = (
                self.grid_pt_2[row][:to_remove]
                + self.grid_pt_2[row][to_remove + 1 : col]
                + ["@"]
                + self.grid_pt_2[row][col:]
            )
            self.grid_pt_2[row][col] = "."

            return RowCol(row, col - 1)

        return RowCol(row, col)

    def up_pt_2(self, row: int, col: int, direc: str) -> RowCol:
        res = self.push_row(row - 1, set([col]), direc)

        if res:
            self.grid_pt_2[row][col] = "."
            return RowCol(row - 1, col)

        return RowCol(row, col)

    def down_pt_2(self, row: int, col: int, direc: str) -> RowCol:
        res = self.push_row(row + 1, set([col]), direc)

        if res:
            self.grid_pt_2[row][col] = "."
            return RowCol(row + 1, col)

        return RowCol(row, col)

    def compaction_pt_2(self, row: int, col: int, direc: str) -> RowCol:
        match direc:
            case ">":
                return self.right_pt_2(row, col)
            case "<":
                return self.left_pt_2(row, col)
            case "^":
                return self.up_pt_2(row, col, direc)
            case "v":
                return self.down_pt_2(row, col, direc)

        return RowCol(row, col)

    def get_pt_1(self) -> str:
        for row in range(self.rows_pt_1):
            for col in range(self.cols_pt_1):
                if self.grid_pt_1[row][col] == "@":
                    cur_row = row
                    cur_col = col

        for move in self.moves:
            cur_row, cur_col = self.compaction_pt_1(cur_row, cur_col, move)

        res = 0
        for row in range(self.rows_pt_1):
            for col in range(self.cols_pt_1):
                if self.grid_pt_1[row][col] == "O":
                    res += (100 * row) + col

        return str(res)

    def get_pt_2(self) -> str:
        for row in range(self.rows_pt_2):
            for col in range(self.cols_pt_2):
                if self.grid_pt_2[row][col] == "@":
                    cur_row = row
                    cur_col = col

        for move in self.moves:
            cur_row, cur_col = self.compaction_pt_2(cur_row, cur_col, move)

        res = 0
        for row in range(self.rows_pt_2):
            for col in range(self.cols_pt_2):
                if self.grid_pt_2[row][col] == "[":
                    inc = (100 * row) + col
                    res += inc

        return str(res)

    def solve(self) -> SolveInfo:
        self.grid_pt_1 = []
        self.grid_pt_2 = []
        self.moves = []

        with open(get_path("15"), encoding="utf-8") as f:
            line = f.readline()

            while line:
                if line == "\n":
                    break

                row = list(line)
                row = row[:-1]

                self.grid_pt_1.append(row)

                row_pt_2 = []
                for c in row:
                    match c:
                        case "#":
                            row_pt_2.extend(["#", "#"])
                        case "O":
                            row_pt_2.extend(["[", "]"])
                        case "@":
                            row_pt_2.extend(["@", "."])
                        case ".":
                            row_pt_2.extend([".", "."])

                self.grid_pt_2.append(row_pt_2)

                line = f.readline()

            line = f.readline()

            while line:
                row = list(line)

                for move in row:
                    if move != "\n":
                        self.moves.append(move)

                line = f.readline()

            self.rows_pt_1 = len(self.grid_pt_1)
            self.cols_pt_1 = len(self.grid_pt_1[0])
            self.rows_pt_2 = len(self.grid_pt_2)
            self.cols_pt_2 = len(self.grid_pt_2[0])

        return SolveInfo(self.get_pt_1(), self.get_pt_2())
