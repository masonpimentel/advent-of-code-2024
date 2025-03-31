"""Helper functions"""

from typing import TextIO, NamedTuple


class GridInfo(NamedTuple):
    """Common components needed for grids"""

    grid: list[list[str]]
    rows: int
    cols: int


def get_grid(f: TextIO) -> GridInfo:
    line = f.readline()

    grid: list[list[str]] = []

    while line:
        row = list(line)
        grid.append(row[:-1] if row[-1] == "\n" else row)
        line = f.readline()

    return GridInfo(grid, len(grid), len(grid[0]))
