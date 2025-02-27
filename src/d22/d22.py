from os.path import join
from collections import deque

class Day22:

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
    
    def ith_secret(self, secret: int, iterations: int) -> int:
        for _ in range(iterations):
            secret = self.generate_new_secret(secret)
        
        return secret

    def get_price_from_secret(self, secret: int) -> int:
        return secret % 10
    
    def get_bananas_from_buyer(self, buyer: dict[str, int], seq: str) -> int:
        if seq in buyer:
            return buyer[seq]
        else:
            return 0

    def sequence_prices(self, secret: int, iterations: int) -> dict[str, int]:
        res: dict[str, int] = {}
        cur_price = self.get_price_from_secret(secret)
        cur_seq: deque[int] = deque([])

        # iterations - 1 because original secret counts as one
        for _ in range(iterations - 1):
            secret = self.generate_new_secret(secret)
            new_price = self.get_price_from_secret(secret)

            this_diff = new_price - cur_price

            cur_seq.append(this_diff)

            if len(cur_seq) > 4:
                cur_seq.popleft()
            
            if len(cur_seq) == 4:
                seq_str = str(cur_seq)

                if seq_str not in res:
                    res[seq_str] = new_price
            
            cur_price = new_price

        return res


    def solve(self):

        with open(
            join('src', 'd22', 'input.txt'), encoding="utf-8"
        ) as f:
            seeds: list[str] = []

            line = f.readline()

            while line:
                seeds.append(line[:-1] if line[-1] == '\n' else line)

                line = f.readline()
            
            pt_1_res = 0

            for seed in seeds:
                r = self.ith_secret(int(seed), 2000)
                pt_1_res += r
            
            buyers: list[dict[str, int]] = []
            all_seqs: set[str] = set()
            for seed in seeds:
                buyer = self.sequence_prices(int(seed), 2000)

                for buyer_seq in buyer:
                    all_seqs.add(buyer_seq)
                
                buyers.append(buyer)
            
            pt_2_res = 0

            for seq in all_seqs:
                this_seq_res = 0

                for buyer in buyers:
                    this_seq_res += self.get_bananas_from_buyer(buyer, seq)
                
                pt_2_res = max(pt_2_res, this_seq_res)

            return (str(pt_1_res), str(pt_2_res))


