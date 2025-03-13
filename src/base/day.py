from abc import ABCMeta, abstractmethod

class Day(metaclass=ABCMeta):
    @abstractmethod
    def solve(self) -> tuple[str, str]: pass