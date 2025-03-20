"""Helper functions"""

from typing import TextIO

def get_grid(f: TextIO) -> tuple[list[list[str]], int, int]:
    line = f.readline()

    grid: list[list[str]] = []

    while line:
        row = list(line)
        grid.append(row[:-1] if row[-1] == "\n" else row)
        line = f.readline()

    return (grid, len(grid), len(grid[0]))
