from collections import defaultdict

from os.path import join

class Day23:
    def solve(self):
        print(f'Runs in ~86.825 (!!) seconds')

        with open(
            join('src', 'd23', 'input.txt'), encoding="utf-8"
        ) as f:
            line = f.readline()

            # aq: yn, vc, cg, wq
            # cg: de, tb, yn, aq
            # yn: aq, cg, wh, td

            adj: dict[str, list[str]] = defaultdict(list)

            while line:
                entry = line[:-1] if line[-1] == '\n' else line[:]

                s = entry.split('-')
                l, r = s[0], s[1]

                adj[l].append(r)
                adj[r].append(l)

                line = f.readline()

            def find_third(first: str, second: str, thirds: str) -> list[str]:
                res: list[str] = []
                
                for third in thirds:
                    third_adj = adj[third]

                    if first in third_adj and second in third_adj:
                        res.append(third)
                
                return res

            tuples: list[list[str]] = []
            seen: set[str] = set()
            for first in adj:
                first_adj = adj[first]
                for i in range(len(first_adj)):
                    second = first_adj[i]

                    for third in find_third(first, second, first_adj[:i] + first_adj[i + 1:]):
                        tpl_l = [first, second, third]
                        tpl_l.sort()
                        tpl_s = str(tpl_l)
                        if tpl_s not in seen:
                            seen.add(tpl_s)
                            tuples.append(tpl_l)

            pt_1_res = 0
            for tpl in tuples:
                for comp in tpl:
                    if comp[0] == 't':
                        pt_1_res += 1
                        break

            self.best: list[str] = []
            self.dp: dict[str, set[str]] = defaultdict(set)
            def rec(so_far: list[str], rem: list[str]):
                # print(f'so_far {so_far} rem {rem}')

                if len(so_far) > len(self.best):
                    self.best = so_far[:]

                sf = sorted(so_far)
                sf = str(sf)
                r = sorted(rem)
                r = str(r)

                if r in self.dp[sf]:
                    return
                self.dp[sf].add(r)

                for i, r in enumerate(rem):
                    add_r = True
                    for to_check in so_far:
                        if r not in adj[to_check]:
                            add_r = False
                            break
                    
                    if add_r:
                        rec(so_far + [r], rem[:i] + rem[i + 1:])
            
            l = len(adj)
            for i, first in enumerate(adj):
                rec([first], adj[first])
            
            self.best.sort()
            
            pt_2_res = ",".join(self.best)
            
            print(f'pt_1_res: {pt_1_res}')
            print(f'pt_2_res: {pt_2_res}')

            return (str(pt_1_res), pt_2_res)

