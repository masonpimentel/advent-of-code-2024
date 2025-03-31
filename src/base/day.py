"""Base Day class"""

from abc import ABCMeta, abstractmethod
from typing import NamedTuple


class SolveInfo(NamedTuple):
    """Expected information from day solvers"""

    pt_1_res: str
    pt_2_res: str


# pylint: disable=R0903,C0115
class Day(metaclass=ABCMeta):
    @abstractmethod
    def solve(self) -> SolveInfo:
        pass
