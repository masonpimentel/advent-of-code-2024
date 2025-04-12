"""Day 22"""

from collections import deque, defaultdict
from typing import NamedTuple
from solvers.base.day import Day
from solvers.base.types import SolveInfo
from solvers.utils.helpers import get_path


# pylint: disable=C0115
class SequenceInfo(NamedTuple):
    final_secret: int
    sequence_prices: defaultdict[str, int]


class Day22(Day):
    """Monkey Market"""

    def mix(self, secret: int, val: int) -> int:
        return secret ^ val

    def prune(self, secret: int) -> int:
        return secret % 16777216

    def generate_new_secret(self, secret: int) -> int:
        mul_64 = secret * 64
        secret = self.mix(secret, mul_64)
        secret = self.prune(secret)

        div_32 = int(secret / 32)
        secret = self.mix(secret, div_32)
        secret = self.prune(secret)

        mul_2048 = secret * 2048
        secret = self.mix(secret, mul_2048)

        return self.prune(secret)

    def get_price_from_secret(self, secret: int) -> int:
        return secret % 10

    def sequence_prices(self, secret: int, iterations: int) -> SequenceInfo:
        cur_price = self.get_price_from_secret(secret)
        cur_seq: deque[int] = deque([])
        seen_seqs_this_buyer: set[str] = set()
        seq_prices: defaultdict[str, int] = defaultdict(int)

        # iterations - 1 for the sequence because original secret counts as one
        for _ in range(iterations - 1):
            secret = self.generate_new_secret(secret)
            new_price = self.get_price_from_secret(secret)

            this_diff = new_price - cur_price
            cur_seq.append(this_diff)

            if len(cur_seq) > 4:
                cur_seq.popleft()

            if len(cur_seq) == 4:
                seq_str = str(cur_seq)

                if seq_str not in seen_seqs_this_buyer:
                    seq_prices[seq_str] += new_price
                    seen_seqs_this_buyer.add(seq_str)

            cur_price = new_price

        # get one more for the iterations-ith secret
        final_secret = self.generate_new_secret(secret)

        return SequenceInfo(final_secret, seq_prices)

    def solve(self) -> SolveInfo:
        pt_1_res = 0

        with open(get_path("22"), encoding="utf-8") as f:
            seeds: list[str] = []

            line = f.readline()
            while line:
                seeds.append(line[:-1] if line[-1] == "\n" else line)
                line = f.readline()

        all_seqs: defaultdict[str, int] = defaultdict(int)
        for seed in seeds:
            secret, seq_prices = self.sequence_prices(int(seed), 2000)

            pt_1_res += secret

            for seq, price in seq_prices.items():
                all_seqs[seq] += price

        pt_2_res = max(all_seqs.values())

        return SolveInfo(str(pt_1_res), str(pt_2_res))
