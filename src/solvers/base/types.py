from typing import NamedTuple


class SolveInfo(NamedTuple):
    """Expected information from day solvers"""

    pt_1_res: str
    pt_2_res: str


class RowCol(NamedTuple):
    row: int
    col: int
